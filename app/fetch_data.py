import grequests
import requests
from time import sleep
from app.profile_handler import get_image_url
from parsel import Selector
from app.face_detection import FaceDetector


def single_fetch_content(github_user: str) -> dict:

    user_dict = dict()
    user_dict["github_username"] = github_user

    gh_profile_url = "https://github.com/" + github_user
    git_response = requests.get(gh_profile_url)
    user_dict["github"] = (
        Selector(text=git_response.text) if git_response.status_code == 200 else None
    )

    readme_response = requests.get(gh_profile_url + "/" + github_user)

    user_dict["github_readme"] = (
        Selector(text=readme_response.text)
        if readme_response.status_code == 200
        else None
    )

    if not user_dict["github"]:
        user_dict["photo_url"] = "https://i.imgur.com/PRiA9r9.png"
    else:
        user_dict["photo_url"] = get_image_url(user_dict["github"])

    photo_response = requests.get(user_dict["photo_url"])

    gh_image_path = "media/" + github_user + "_image.jpg"

    with open(gh_image_path, "wb") as handler:
        handler.write(photo_response.content)
        user_dict["photo"] = FaceDetector.find_faces(gh_image_path)

    return user_dict

def group_fetch_content(user_dicts: list[str]) -> list:

    user_dicts = [{'github_username': user} for user in user_dicts]

    gh_profile_urls = ["https://github.com/" + user['github_username'] for user in user_dicts]
    rs = (grequests.get(u) for u in gh_profile_urls)
    git_responses = grequests.map(rs)
    sleep(1)
    readmes_profile_urls = ["https://github.com/" + user['github_username'] + '/' + user['github_username'] for user in user_dicts]
    rs = (grequests.get(u) for u in readmes_profile_urls)
    readme_responses = grequests.map(rs)
    sleep(1)

    for index in range(len(user_dicts)):
    
        user_dicts[index]["github"] = (
            Selector(text=git_responses[index].text) if git_responses[index].status_code == 200 else None
        )

        user_dicts[index]["github_readme"] = (
            Selector(text=readme_responses[index].text)
            if readme_responses[index].status_code == 200
            else None
        )

        if not user_dicts[index]["github"]:
            user_dicts[index]['photo_url'] = "https://i.imgur.com/PRiA9r9.png"
        else:
            user_dicts[index]['photo_url'] = get_image_url(user_dicts[index]["github"])
        
    photos_urls = [user['photo_url'] for user in user_dicts]
    rs = (grequests.get(u) for u in photos_urls)
    photo_responses = grequests.map(rs)
    sleep(1)

    for index in range(len(user_dicts)):
    
        gh_image_path = "media/" + user_dicts[index]['github_username'] + "_image.jpg"

        with open(gh_image_path, "wb") as handler:
            handler.write(photo_responses[index].content)
            user_dicts[index]["photo"] = FaceDetector.find_faces(gh_image_path)

    return user_dicts

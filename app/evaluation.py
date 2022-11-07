from app.fetch_data import group_fetch_content
from app.data_getter import populate_dicts


def single_evaluation(user_dict: dict) -> dict:
    user_dict["has_five_tags"] = False
    user_dict["has_ten_tags"] = False
    user_dict["has_five_repos"] = False
    user_dict["has_ten_repos"] = False
    user_dict["has_two_pinned"] = False
    user_dict["has_four_pinned"] = False

    if not user_dict["github"]:
        user_dict["grade"] = 0
        user_dict["readme"] = False
        user_dict["linkedin"] = False
        user_dict["email"] = False
        user_dict["tags"] = 0
        user_dict["repos"] = 0
        user_dict["pinned"] = 0
        return user_dict
    
    grade = 0

    if user_dict["photo"]:
        grade += 10

    if user_dict["email"]:
        grade += 10

    if user_dict["linkedin"]:
        grade += 10

    if user_dict["readme"]:
        grade += 10
        if user_dict["tags"] >= 5:
            grade += 10
            user_dict["has_five_tags"] = True

            if user_dict["tags"] >= 10:
                grade += 10
                user_dict["has_ten_tags"] = True

    if user_dict["repos"] >= 5:
        grade += 10
        user_dict["has_five_repos"] = True

        if user_dict["repos"] >= 10:
            grade += 10
            user_dict["has_ten_repos"] = True

    if user_dict["pinned"] >= 2:
        grade += 10
        user_dict["has_two_pinned"] = True

        if user_dict["pinned"] >= 4:
            grade += 10
            user_dict["has_four_pinned"] = True

    user_dict["grade"] = grade

    del user_dict['github']
    del user_dict['github_readme']

    return user_dict


def do_group_evaluation(general_list_of_dicts):
    general_list_of_dicts = populate_dicts(group_fetch_content(general_list_of_dicts))
    for index, each_dict in enumerate(general_list_of_dicts):
        general_list_of_dicts[index] = single_evaluation(each_dict)

    return general_list_of_dicts

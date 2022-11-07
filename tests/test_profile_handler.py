from app.profile_handler import get_image_url
from app.fetch_data import single_fetch_content

valid_profile = single_fetch_content('felipmartins')
invalid_profile = single_fetch_content('akjsdnaljsbhfljkashfjashd')

def test_get_urls():
    assert get_image_url(valid_profile['github']) != 'https://i.imgur.com/PRiA9r9.png'
    assert 'avatars.githubusercontent' in get_image_url(valid_profile['github'])
    assert get_image_url(invalid_profile['github']) == None

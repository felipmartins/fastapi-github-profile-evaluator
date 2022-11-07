from app.fetch_data import group_fetch_content
from app.utils import csv_to_list

def test_group_fetch_content():
    csv_list = csv_to_list('mocks/csv_mock.csv')
    string_list = [user['github_username'] for user in csv_list]
    response = group_fetch_content(string_list)
    assert len(response) == 3
    assert response[0]['github_username'] == 'felipmartins'
    assert len(response[0]) == 5



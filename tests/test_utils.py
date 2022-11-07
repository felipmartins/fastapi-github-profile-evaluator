from app.utils import csv_to_list


def test_csv_to_list_method_works():
    assert csv_to_list("mocks/csv_mock.csv") == [
        {"github_username": "felipmartins"},
        {"github_username": "vbuxbaum"},
        {"github_username": "ipfalvim"},
    ]

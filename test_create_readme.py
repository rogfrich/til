import os
from create_readme import get_categories, ignored_directories, get_data


def test_get_categories():
    categories = get_categories()
    assert isinstance(categories, list)
    for item in categories:
        assert item in os.listdir(".") and item not in ignored_directories


def test_get_data_returns_dict():
    categories = get_categories()
    assert isinstance(get_data(categories), dict)


def test_get_data_excludes_test_directories():
    categories = get_categories()
    data = get_data(categories)
    for i in ("test_category1", "test_category2"):
        assert i not in data.keys()


def test_get_data_returns_correct_values():
    valid_data = {
        "test_category1": [('CAT 1 - ARTICLE 1', 'test_category1/test_cat1_article1.md'), ('CAT 1 - ARTICLE 2', 'test_category1/test_cat1_article2.md')],
        "test_category2": [('CAT 2 - ARTICLE 1', 'test_category2/test_cat2_article1.md'), ('CAT 2 - ARTICLE 2', 'test_category2/test_cat2_article2.md')],
    }

    test_categories = ["test_category1", "test_category2"]
    data = get_data(test_categories)
    assert data == valid_data

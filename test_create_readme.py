import os
from create_readme import get_categories, ignored_directories

def test_get_categories():
    categories = get_categories()
    assert isinstance(categories, list)
    for item in categories:
        assert item in os.listdir(".") and item not in ignored_directories


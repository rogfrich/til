import os, subprocess
from create_readme import (
    get_categories,
    get_data,
    get_things_learned_count,
    convert_spaces_to_dashes,
)


def test_local_repo_is_up_to_date():
    """
    Make sure that the local repo is up to date with the remote - if not, we'll lose any changes to the remote when we
    regenerate the file.
    """
    subprocess.run(["git", "fetch"])
    git_status = str(subprocess.check_output(["git", "status"]))
    assert "branch is behind" not in git_status


def test_get_categories():
    categories = get_categories()
    assert isinstance(categories, list)
    for item in categories:
        assert item in os.listdir("./content")


def test_get_data_returns_dict():
    categories = get_categories()
    assert isinstance(get_data(categories), dict)


def test_get_data_returns_correct_values():
    valid_data = {
        "test_category1": [
            ("CAT 1 - ARTICLE 1", "./content/test_category1/test_cat1_article1.md"),
            ("CAT 1 - ARTICLE 2", "./content/test_category1/test_cat1_article2.md"),
        ],
        "test_category2": [
            ("CAT 2 - ARTICLE 1", "./content/test_category2/test_cat2_article1.md"),
            ("CAT 2 - ARTICLE 2", "./content/test_category2/test_cat2_article2.md"),
        ],
    }

    test_categories = ["test_category1", "test_category2"]
    data = get_data(test_categories)
    assert data == valid_data


def test_things_learned_count():
    categories = get_categories()
    data = get_data(categories)
    correct_count = 0
    for v in data.values():
        correct_count += len(v)

    assert get_things_learned_count(data) == correct_count


def test_convert_spaces_to_dashes():
    test_string = "I am a string"
    assert convert_spaces_to_dashes(test_string) == "I-am-a-string"

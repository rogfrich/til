import os

ignored_directories = [
    "docs",
    "venv",
    ".git",
    ".idea",
    ".pytest_cache",
    "__pycache__",
    "test_category1",
    "test_category2",
]


def get_categories():
    categories = [
        category for category in os.listdir(".") if os.path.isdir(category) and category not in ignored_directories
    ]
    return sorted(categories)


def get_data(categories: list):
    data = {}
    for category in categories:
        articles_in_category = []
        for file in sorted(os.listdir(category)):
            with open(os.path.join(category, file)) as f:
                for line in f:
                    if line.startswith("#"):
                        articles_in_category.append(
                            (line[1:].strip(), os.path.join(category, file))
                        )
                        break
        data[category] = articles_in_category
    return data


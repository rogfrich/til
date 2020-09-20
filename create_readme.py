import os

ignored_directories = ['docs', 'venv', '.git', '.idea', '.pytest_cache', '__pycache__']


def get_categories():
    categories = [
        x for x in os.listdir(".") if os.path.isdir(x) and x not in ignored_directories
    ]
    return sorted(categories)

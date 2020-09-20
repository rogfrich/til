import os
from template import HEADER


ignored_directories = [
    "docs",
    "venv",
    ".git",
    ".idea",
    ".pytest_cache",
    "__pycache__",
    # test_category1",
    # test_category2",
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


def write_output(data: dict):
    with open("test_output.md", mode='w') as fout:
        # Write header
        fout.write(HEADER)

        # Write list of categories:
        for category in data.keys():
            fout.write(f"- [{category.upper()}](./{category})\n")



        # Write index of articles:
        fout.write("## Articles\n")
        for k, v in data.items():
            fout.write(f"\n{k.upper()}\n")
            for title_file_pair in v:
                title = title_file_pair[0]
                file = title_file_pair[1]
                fout.write(f"- [{title}]({file})\n")


c = get_categories()
d = get_data(c)
write_output(d)

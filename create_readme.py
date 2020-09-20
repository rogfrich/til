import os
from template import HEADER, FOOTER

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


def write_output(data: dict):
    with open("readme.md", mode='w') as fout:
        # Write header
        fout.write(HEADER)

        # Write list of categories:
        for category in data.keys():
            fout.write(f"- [{category}](./{category})\n")

        fout.write("----")

        # Write index of articles:
        for k, v in data.items():
            fout.write(f"\n{k}\n")
            for title_file_pair in v:
                title = title_file_pair[0]
                file = title_file_pair[1]
                fout.write(f"- [{title}]({file})\n")

        # write footer
        fout.write(FOOTER)


categories = get_categories()
data = get_data(categories)
write_output(data)
print(data)
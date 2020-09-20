import os
from template import HEADER, FOOTER


def get_categories():
    for folder, subfolders, files in os.walk("."):
        if folder == './content':
            return sorted([x for x in subfolders if not x.startswith("test")])


def get_data(categories: list):
    data = {}
    basepath = './content'
    for category in categories:
        articles_in_category = []
        for file in sorted(os.listdir(os.path.join(basepath, category))):
            with open(os.path.join(basepath, category, file)) as f:
                for line in f:
                    if line.startswith("#"):
                        articles_in_category.append(
                            (line[1:].strip(), os.path.join(basepath, category, file))
                        )
                        break
        data[category] = articles_in_category
    return data


def write_output(data: dict):
    with open("readme.md", mode='w') as fout:
        fout.write(HEADER)

        # Write list of categories:
        for category in data.keys():
            fout.write(f"- [{category}](./content/{category})\n")

        fout.write("----")

        # Write index of articles:
        for k, v in data.items():
            fout.write(f"\n{k}\n")
            for title_file_pair in v:
                title = title_file_pair[0]
                file = title_file_pair[1]
                fout.write(f"- [{title}]({file})\n")

        fout.write(FOOTER)


if __name__ == '__main__':
    categories = get_categories()
    data = get_data(categories)
    write_output(data)

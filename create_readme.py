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


def get_things_learned_count(data: dict):
    things_learned_count = 0
    for value in data.values():
        things_learned_count += len(value)

    return things_learned_count


def convert_spaces_to_dashes(text: str) -> str:
    split_text = text.split()
    return "-".join(split_text)


def write_output(data: dict):
    with open("readme.md", mode='w') as fout:
        fout.write(HEADER)
        fout.write(f"So far, I have learned {get_things_learned_count(data)} things.\n\n")
        # Write list of categories:
        fout.write('## Categories\n')
        for category in data.keys():
            fout.write(
                f"- [{category}](<#{convert_spaces_to_dashes(category)}>)\n")

        fout.write("----")

        # Write index of articles:
        for k, v in data.items():
            fout.write(f"\n### {k}\n")
            for title_file_pair in sorted(v):
                title = title_file_pair[0]
                file = title_file_pair[1]
                fout.write(f"- [{title}](<{file}>)\n")

        fout.write(FOOTER)


if __name__ == '__main__':
    categories = get_categories()
    data = get_data(categories)
    write_output(data)

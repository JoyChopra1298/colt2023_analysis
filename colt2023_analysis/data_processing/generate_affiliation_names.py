import json

from constants.file_names import STRUCTURED_DATA_FILE_PATH, AFFILIATION_NAMES_FILE_PATH


def generate_affiliation_names():
    affiliation_dictionary = {}
    with open("../../" + STRUCTURED_DATA_FILE_PATH, "r") as structured_data_file:
        data_dictionary = json.load(structured_data_file)
        for paper_id, paper_data in data_dictionary.items():
            authors = paper_data["authors"]
            for author in authors:
                author_affiliation = author["affiliation_name"]
                if author_affiliation not in affiliation_dictionary:
                    affiliation_dictionary[author_affiliation] = 1

    with open("../../" + AFFILIATION_NAMES_FILE_PATH, "w") as affiliation_names_file:
        for affiliation_name in sorted(affiliation_dictionary.keys()):
            affiliation_names_file.write(affiliation_name + "\n")


if __name__ == "__main__":
    generate_affiliation_names()

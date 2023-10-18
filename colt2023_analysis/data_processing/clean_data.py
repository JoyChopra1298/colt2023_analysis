import json

from constants.affiliations import AFFILIATION_MAP, UNKNOWN_AFFILIATIONS, UNKNOWN_AFFILIATION_WORD
from constants.file_names import STRUCTURED_DATA_FILE_PATH, CLEANED_DATA_FILE_PATH


def merge_affiliation_names(data_dictionary):
    for paper_id, paper_data in data_dictionary.items():
        authors = paper_data["authors"]
        for author in authors:
            author_affiliation = author["affiliation_name"]
            if author_affiliation in AFFILIATION_MAP:
                author["affiliation_name"] = AFFILIATION_MAP[author_affiliation]


def mark_unknown_affiliations(data_dictionary):
    for paper_id, paper_data in data_dictionary.items():
        authors = paper_data["authors"]
        for author in authors:
            author_affiliation = author["affiliation_name"]
            if author_affiliation in UNKNOWN_AFFILIATIONS:
                author["affiliation_name"] = UNKNOWN_AFFILIATION_WORD


def clean_data():
    with open("../../" + STRUCTURED_DATA_FILE_PATH, "r") as structured_data_file:
        data_dictionary = json.load(structured_data_file)
        merge_affiliation_names(data_dictionary)
        mark_unknown_affiliations(data_dictionary)

    with open("../../" + CLEANED_DATA_FILE_PATH, "w") as cleaned_data_file:
        json.dump(data_dictionary, cleaned_data_file, indent=4)


if __name__ == "__main__":
    clean_data()

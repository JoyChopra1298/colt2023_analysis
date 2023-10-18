import json

from constants.file_names import STRUCTURED_DATA_FILE_PATH


def merge_affiliation_names():
    pass


def mark_unknown_affiliations(data_dictionary):
    pass

def clean_data():
    with open("../../" + STRUCTURED_DATA_FILE_PATH, "r") as structured_data_file:
        data_dictionary = json.load(structured_data_file)
        mark_unknown_affiliations(data_dictionary)
        merge_affiliation_names()


if __name__ == "__main__":
    clean_data()

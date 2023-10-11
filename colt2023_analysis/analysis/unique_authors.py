import json

from constants.file_names import STRUCTURED_DATA_FILE_PATH
from utils.general_utils import sort_dictionary_by_values


def unique_authors_analysis():
    with open("../../" + STRUCTURED_DATA_FILE_PATH, "r") as structured_data_file:
        paper_data_dictionary = json.load(structured_data_file)
        authors_dictionary = {}
        for paper_id, paper_data in paper_data_dictionary.items():
            authors = paper_data["authors"]
            for author in authors:
                author_name = author["author_name"]
                if author_name not in authors_dictionary:
                    authors_dictionary[author_name] = 1
                else:
                    authors_dictionary[author_name] += 1
        print("Number of unique authors: ", len(authors_dictionary))


if __name__ == "__main__":
    unique_authors_analysis()

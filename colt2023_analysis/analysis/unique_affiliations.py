import json

from constants.file_names import STRUCTURED_DATA_FILE_PATH


def unique_affiliations_analysis():
    with open("../../" + STRUCTURED_DATA_FILE_PATH, "r") as structured_data_file:
        paper_data_dictionary = json.load(structured_data_file)
        authors_dictionary = {}
        for paper_id, paper_data in paper_data_dictionary.items():
            authors = paper_data["authors"]
            for author in authors:
                author_affiliation = author["affiliation_name"]
                if author_affiliation not in authors_dictionary:
                    authors_dictionary[author_affiliation] = 1
        print("Number of unique affiliations: ", len(authors_dictionary))


if __name__ == "__main__":
    unique_affiliations_analysis()

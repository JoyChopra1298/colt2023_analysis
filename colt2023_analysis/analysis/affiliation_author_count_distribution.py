import json

from constants.file_names import STRUCTURED_DATA_FILE_PATH
from utils.general_utils import sort_dictionary_by_values, sort_dictionary_by_keys

NUMBER_OF_TOP_AFFILIATIONS = 11


def print_top_affiliations(affiliations_dictionary):
    sorted_affiliations_list = sort_dictionary_by_values(affiliations_dictionary, reverse=True)
    for affiliation_index in range(0, NUMBER_OF_TOP_AFFILIATIONS):
        affiliation_details = sorted_affiliations_list[affiliation_index]
        print(f"{affiliation_index + 1}. {affiliation_details[0]} - {affiliation_details[1]} authors")


def print_affiliation_author_count_distribution(affiliations_dictionary):
    author_count_affiliation_count_dictionary = {}
    for _, author_count in affiliations_dictionary.items():
        if author_count in author_count_affiliation_count_dictionary:
            author_count_affiliation_count_dictionary[author_count] += 1
        else:
            author_count_affiliation_count_dictionary[author_count] = 1
    sorted_paper_count_author_count_list = sort_dictionary_by_keys(author_count_affiliation_count_dictionary)
    for item_index in range(0, len(sorted_paper_count_author_count_list)):
        item = sorted_paper_count_author_count_list[item_index]
        author_count = item[0]
        affiliation_count = item[1]
        print(f"{item_index + 1}. Number of affiliations with {author_count} authors - {affiliation_count}")


def generate_authors_dictionary(paper_data_dictionary):
    COMBINED_KEY_SEPARATOR = "#"
    affiliations_authors_dictionary = {}
    for paper_id, paper_data in paper_data_dictionary.items():
        authors = paper_data["authors"]
        for author in authors:
            author_name = author["author_name"]
            affiliation_name = author["affiliation_name"]
            combined_key = author_name + COMBINED_KEY_SEPARATOR + affiliation_name
            # Remove duplicate author affiliation combinations. Count each unique pair once
            if combined_key not in affiliations_authors_dictionary:
                affiliations_authors_dictionary[combined_key] = 1

    affiliations_dictionary = {}
    for combined_key in affiliations_authors_dictionary:
        separated_key = combined_key.split(COMBINED_KEY_SEPARATOR)
        affiliation_name = separated_key[1]
        if affiliation_name not in affiliations_dictionary:
            affiliations_dictionary[affiliation_name] = 1
        else:
            affiliations_dictionary[affiliation_name] += 1
    return affiliations_dictionary


def affiliation_author_count_analysis():
    with open("../../" + STRUCTURED_DATA_FILE_PATH, "r") as structured_data_file:
        paper_data_dictionary = json.load(structured_data_file)
        affiliations_dictionary = generate_authors_dictionary(paper_data_dictionary)
        print_top_affiliations(affiliations_dictionary)
        print()
        print_affiliation_author_count_distribution(affiliations_dictionary)


if __name__ == "__main__":
    affiliation_author_count_analysis()

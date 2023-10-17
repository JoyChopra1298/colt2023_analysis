import json

from constants.file_names import STRUCTURED_DATA_FILE_PATH
from utils.general_utils import sort_dictionary_by_values, sort_dictionary_by_keys

NUMBER_OF_TOP_AFFILIATIONS = 10


def print_top_affiliations(affiliations_dictionary):
    sorted_affiliations_list = sort_dictionary_by_values(affiliations_dictionary, reverse=True)
    for affiliation_index in range(0, NUMBER_OF_TOP_AFFILIATIONS):
        affiliation_details = sorted_affiliations_list[affiliation_index]
        print(f"{affiliation_index + 1}. {affiliation_details[0]} - {affiliation_details[1]} papers")


def print_affiliation_paper_count_distribution(affiliations_dictionary):
    paper_count_affiliation_count_dictionary = {}
    for paper_count in affiliations_dictionary.values():
        if paper_count in paper_count_affiliation_count_dictionary:
            paper_count_affiliation_count_dictionary[paper_count] += 1
        else:
            paper_count_affiliation_count_dictionary[paper_count] = 1
    sorted_paper_count_author_count_list = sort_dictionary_by_keys(paper_count_affiliation_count_dictionary)
    for item_index in range(0, len(sorted_paper_count_author_count_list)):
        item = sorted_paper_count_author_count_list[item_index]
        paper_count = item[0]
        affiliation_count = item[1]
        print(f"{item_index + 1}. Number of affiliations with {paper_count} papers - {affiliation_count}")


def generate_affiliations_dictionary(paper_data_dictionary):
    COMBINED_KEY_SEPARATOR = "#"
    affiliations_papers_dictionary = {}
    for paper_id, paper_data in paper_data_dictionary.items():
        authors = paper_data["authors"]
        for author in authors:
            affiliation_name = author["affiliation_name"]
            combined_key = paper_id + COMBINED_KEY_SEPARATOR + affiliation_name
            # Remove duplicate paper affiliation combinations. Count each unique pair once
            if combined_key not in affiliations_papers_dictionary:
                affiliations_papers_dictionary[combined_key] = 1

    affiliations_dictionary = {}
    for combined_key in affiliations_papers_dictionary:
        separated_key = combined_key.split(COMBINED_KEY_SEPARATOR)
        affiliation_name = separated_key[1]
        if affiliation_name not in affiliations_dictionary:
            affiliations_dictionary[affiliation_name] = 1
        else:
            affiliations_dictionary[affiliation_name] += 1
    return affiliations_dictionary


def affiliation_paper_count_analysis():
    with open("../../" + STRUCTURED_DATA_FILE_PATH, "r") as structured_data_file:
        paper_data_dictionary = json.load(structured_data_file)
        affiliations_dictionary = generate_affiliations_dictionary(paper_data_dictionary)
        print_top_affiliations(affiliations_dictionary)
        print()
        print_affiliation_paper_count_distribution(affiliations_dictionary)


if __name__ == "__main__":
    affiliation_paper_count_analysis()

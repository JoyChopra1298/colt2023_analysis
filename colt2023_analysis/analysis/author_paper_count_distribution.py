import json

from constants.file_names import CLEANED_DATA_FILE_PATH
from utils.general_utils import sort_dictionary_by_values, sort_dictionary_by_keys

NUMBER_OF_TOP_AUTHORS = 11


def print_top_authors(authors_dictionary):
    sorted_authors_list = sort_dictionary_by_values(authors_dictionary, reverse=True)
    for author_index in range(0, NUMBER_OF_TOP_AUTHORS):
        author_details = sorted_authors_list[author_index]
        print(f"{author_index + 1}. {author_details[0]} - {author_details[1]} papers")


def print_author_paper_count_distribution(authors_dictionary):
    paper_count_author_count_dictionary = {}
    for paper_count in authors_dictionary.values():
        if paper_count in paper_count_author_count_dictionary:
            paper_count_author_count_dictionary[paper_count] += 1
        else:
            paper_count_author_count_dictionary[paper_count] = 1
    sorted_paper_count_author_count_list = sort_dictionary_by_keys(paper_count_author_count_dictionary)
    for item_index in range(0, len(sorted_paper_count_author_count_list)):
        item = sorted_paper_count_author_count_list[item_index]
        paper_count = item[0]
        author_count = item[1]
        print(f"{item_index + 1}. Number of author with {paper_count} accepted papers - {author_count}")


def generate_authors_dictionary(paper_data_dictionary):
    authors_dictionary = {}
    for paper_id, paper_data in paper_data_dictionary.items():
        authors = paper_data["authors"]
        for author in authors:
            author_name = author["author_name"]
            if author_name not in authors_dictionary:
                authors_dictionary[author_name] = 1
            else:
                authors_dictionary[author_name] += 1
    return authors_dictionary


def author_paper_count_analysis():
    with open("../../" + CLEANED_DATA_FILE_PATH, "r") as data_file:
        paper_data_dictionary = json.load(data_file)
        authors_dictionary = generate_authors_dictionary(paper_data_dictionary)
        print_top_authors(authors_dictionary)
        print()
        print_author_paper_count_distribution(authors_dictionary)


if __name__ == "__main__":
    author_paper_count_analysis()

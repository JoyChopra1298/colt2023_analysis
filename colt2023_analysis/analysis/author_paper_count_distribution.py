import json

from constants.file_names import STRUCTURED_DATA_FILE_PATH
from utils.general_utils import sort_dictionary_by_values

NUMBER_OF_TOP_AUTHORS = 10

def author_paper_count_analysis():
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
        sorted_authors_list = sort_dictionary_by_values(authors_dictionary, reverse=True)
        for author_index in range(0, NUMBER_OF_TOP_AUTHORS):
            author_details = sorted_authors_list[author_index]
            print(f"{author_index + 1}. {author_details[0]} - {author_details[1]} papers")


if __name__ == "__main__":
    author_paper_count_analysis()

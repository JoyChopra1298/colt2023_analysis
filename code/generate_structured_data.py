import json
import re

# Convert each line to JSON
# Write output file

RAW_DATA_FILE_PATH = "../data/raw_data.txt"
STRUCTURED_DATA_FILE_PATH = "../data/structured_data.json"
NUMBER_OF_LINES_PER_PAPER = 2

# First group is author name, second group is affiliation name
AUTHOR_DATA_REGEX_PATTERN = "(.*) \((.*)\)"


def extract_paper_data(paper_id, raw_data):
    paper_data = {
        "paper_id": paper_id,
        "paper_title": raw_data[0]
    }
    author_data_list = []
    author_raw_data_list = raw_data[1].split(";")
    for author_raw_data in author_raw_data_list:
        author_data_split_list = re.split(AUTHOR_DATA_REGEX_PATTERN, author_raw_data)
        author_data = {
            "author_name": author_data_split_list[1],
            "affiliation_name": author_data_split_list[2]
        }
        author_data_list.append(author_data)
    paper_data["authors"] = author_data_list
    return paper_data


def generate_structured_data():
    paper_data_dictionary = {}
    with open(RAW_DATA_FILE_PATH, "r") as raw_data_file:
        raw_data = raw_data_file.read().split("\n")
        number_of_papers = int(len(raw_data) / NUMBER_OF_LINES_PER_PAPER)
        for paper_index in range(0, number_of_papers):
            array_index = paper_index * NUMBER_OF_LINES_PER_PAPER
            paper_id = paper_index + 1
            paper_data = extract_paper_data(paper_id,
                                            raw_data[array_index: array_index + NUMBER_OF_LINES_PER_PAPER])
            paper_data_dictionary[paper_id] = paper_data

    with open(STRUCTURED_DATA_FILE_PATH, "w") as structured_data_file:
        json.dump(paper_data_dictionary, structured_data_file, indent=4)


if __name__ == "__main__":
    generate_structured_data()

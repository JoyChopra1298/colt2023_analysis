# Basic analysis for COLT 2023 papers 
Code to analyse accepted papers at COLT 2023

Link to accepted papers - https://learningtheory.org/colt2023/accepted-papers.html

The file `data/raw_data.txt` contains raw data copied from above link. Each paper is represented by 2 lines. The first line is the name of the paper and the second line is a list of name of authors

There are total 330 lines in `data_raw_data.txt` which indicates that there are 330/2 = 165 papers which were accepted in COLT 2023

The structured data contains each paper in following JSON format
```
{
    "paper_id": Index of paper in the raw data,
    "paper_title": Title of the paper
    "authors": [
        {
            "author_name": Name of the author
            "affiliation_name": Name of author's affiliation
        }
    ]
}
```

Results of basic analysis
1. There are 165 accepted papers
2. There are 438 unique authors
3. There are 173 unique affiliations
4. Steve Hanneke is the author with highest number of accepted papers. He has 7 accepted papers.

Distribution of paper count and author counts
1. Number of author with 1 accepted papers - 373
2. Number of author with 2 accepted papers - 54
3. Number of author with 3 accepted papers - 4
4. Number of author with 4 accepted papers - 3
5. Number of author with 6 accepted papers - 3
6. Number of author with 7 accepted papers - 1

There are 11 authors with 3 or more papers.
1. Steve Hanneke - 7 papers
2. Yury Polyanskiy - 6 papers
3. Shay Moran - 6 papers
4. Ilias Diakonikolas - 6 papers
5. Constantinos Daskalakis - 4 papers
6. Dylan J Foster - 4 papers
7. Noah Golowich - 4 papers
8. Nikita Zhivotovskiy - 3 papers
9. Nikos Zarifis - 3 papers
10. Alexander S Wein - 3 papers
11. Kaiqing Zhang - 3 papers

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
Note - data cleaning has not been done

Results of basic analysis
1. There are 165 accepted papers
2. There are 438 unique authors
3. There are 173 unique affiliations
4. Steve Hanneke is the author with highest number of accepted papers. He has 7 accepted papers.
5. MIT is the affiliation with highest number of authors. It has 29 authors.

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

Distribution of author count and affiliation counts
1. Number of affiliations with 1 authors - 98
2. Number of affiliations with 2 authors - 26
3. Number of affiliations with 3 authors - 20
4. Number of affiliations with 4 authors - 6
5. Number of affiliations with 5 authors - 6
6. Number of affiliations with 6 authors - 4
7. Number of affiliations with 7 authors - 2
8. Number of affiliations with 8 authors - 2
9. Number of affiliations with 9 authors - 3
10. Number of affiliations with 10 authors - 1
11. Number of affiliations with 11 authors - 1
12. Number of affiliations with 13 authors - 1
13. Number of affiliations with 15 authors - 1
14. Number of affiliations with 19 authors - 1
15. Number of affiliations with 29 authors - 1

There are 11 affiliations with 8 or more authors
1. MIT - 29 authors
2. Google - 19 authors
3. Stanford University - 15 authors
4. EPFL - 13 authors
5. UC Berkeley - 11 authors
6. University of Wisconsin-Madison - 10 authors
7. Cornell University - 9 authors
8. University of Texas at Austin - 9 authors
9. Georgia Institute of Technology - 9 authors
10. Massachusetts Institute of Technology - 8 authors
11. Technion - 8 authors

Distribution of paper count and affiliation counts
1. Number of affiliations with 1 papers - 108
2. Number of affiliations with 2 papers - 27
3. Number of affiliations with 3 papers - 17
4. Number of affiliations with 4 papers - 5
5. Number of affiliations with 5 papers - 3
6. Number of affiliations with 6 papers - 3
7. Number of affiliations with 7 papers - 2
8. Number of affiliations with 8 papers - 1
9. Number of affiliations with 9 papers - 1
10. Number of affiliations with 10 papers - 2
11. Number of affiliations with 11 papers - 1
12. Number of affiliations with 12 papers - 2
13. Number of affiliations with 28 papers - 1

There are 10 affiliations with more than 6 authors
1. MIT - 28 papers
2. Massachusetts Institute of Technology - 12 papers
3. Stanford University - 12 papers
4. Google - 11 papers
5. UC Berkeley - 10 papers
6. University of Wisconsin-Madison - 10 papers
7. Purdue University - 9 papers
8. EPFL - 8 papers
9. University of Washington - 7 papers
10. Microsoft Research - 7 papers

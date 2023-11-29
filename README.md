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
Note - data has been partially cleaned

Results of basic analysis
1. There are 165 accepted papers
2. There are 438 unique authors
3. There are 131 unique affiliations
4. Steve Hanneke is the author with highest number of accepted papers. He has 7 accepted papers.
5. MIT is the affiliation with highest number of authors. It has 29 authors.
6. MIT is the affiliation with highest number of papers. It has 28 papers.

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
1. Number of affiliations with 1 authors - 63
2. Number of affiliations with 2 authors - 17
3. Number of affiliations with 3 authors - 18
4. Number of affiliations with 4 authors - 7
5. Number of affiliations with 5 authors - 4
6. Number of affiliations with 6 authors - 3
7. Number of affiliations with 7 authors - 8
8. Number of affiliations with 8 authors - 1
9. Number of affiliations with 9 authors - 2
10. Number of affiliations with 10 authors - 1
11. Number of affiliations with 12 authors - 1
12. Number of affiliations with 13 authors - 1
13. Number of affiliations with 14 authors - 1
14. Number of affiliations with 15 authors - 1
15. Number of affiliations with 18 authors - 1
16. Number of affiliations with 22 authors - 1
17. Number of affiliations with 38 authors - 1

There are 10 affiliations with 9 or more authors
1. Massachusetts Institute of Technology - 38 authors
2. Google - 22 authors
3. Stanford University - 18 authors
4. University of Wisconsin-Madison - 15 authors
5. Georgia Institute of Technology - 14 authors
6. EPFL - 13 authors
7. University of California, Berkeley - 12 authors
8. Cornell University - 10 authors
9. University of Texas at Austin - 9 authors
10. Technion - Israel Institute of Technology - 9 authors

Distribution of paper count and affiliation counts
1. Number of affiliations with 1 papers - 76
2. Number of affiliations with 2 papers - 18
3. Number of affiliations with 3 papers - 13
4. Number of affiliations with 4 papers - 4
5. Number of affiliations with 5 papers - 4
6. Number of affiliations with 6 papers - 3
7. Number of affiliations with 7 papers - 3
8. Number of affiliations with 8 papers - 3
9. Number of affiliations with 9 papers - 2
10. Number of affiliations with 11 papers - 2
11. Number of affiliations with 13 papers - 2
12. Number of affiliations with 29 papers - 1

There are 10 affiliations with 8 or more papers
1. Massachusetts Institute of Technology - 29 papers
2. Google - 13 papers
3. Stanford University - 13 papers
4. University of California, Berkeley - 11 papers
5. University of Wisconsin-Madison - 11 papers
6. Purdue University - 9 papers
7. Georgia Institute of Technology - 9 papers
8. Microsoft - 8 papers
9. Unknown - 8 papers
10. EPFL - 8 papers

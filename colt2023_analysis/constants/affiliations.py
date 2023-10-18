"""
This map contains mapping from similar affiliation names to a single standard affiliation name
"""
AFFILIATION_MAP = {
    "Amazon Science": "Amazon",
    "Ben-Gurion University": "Ben-Gurion University of the Negev",
    "CMU": "Carnegie Mellon University",
    "CORNELL UNIVERSITY": "Cornell University",
    "Columbia": "Columbia University",
    "ETH ZURICH": "ETH Zurich",
    "ETH Zürich": "ETH Zurich",
    "Georgia Institute of Technolog": "Georgia Institute of Technology",
    "Georgia Tech": "Georgia Institute of Technology",
    "Google Research": "Google",
    "Harvard": "Harvard University",
    "IISc), Bangalore": "Indian Institute of Science",
    "-MIT": "Massachusetts Institute of Technology",
    "MIT": "Massachusetts Institute of Technology",
    "Microsoft Research": "Microsoft",
    "Microsoft Research Asia": "Microsoft",
    "Meta AI": "Facebook",
    "Meta FAIR Labs": "Facebook",
    "Princeton": "Princeton University",
    "Princeton.edu": "Princeton University",
    "Stanford": "Stanford University",
    "Stanford University, California": "Stanford University",
    "Technion": "Technion - Israel Institute of Technology",
    "Toyota Technical Institute of Chicago": "Toyota Technological Institute at Chicago",
    "\" Tsinghua University, China\"": "Tsinghua University",
    "Tsinghua Unversity": "Tsinghua University",
    "USC": "University of Southern California",
    "University of southern California": "University of Southern California",
    "U. of Southern California": "University of Southern California",
    "UCI": "University of California, Irvine",
    "UC Irvine": "University of California, Irvine",
    "UC Berkeley": "University of California, Berkeley",
    "UCSD": "University of California San Diego",
    "UCSB": "University of California Santa Barbara",
    "UC Davis": "University of California, Davis",
    "UCLA": "University of California, Los Angeles",
    "University of Toronto, Vector Institute": "University of Toronto",
    "University of Wisconsin - Madison": "University of Wisconsin-Madison",
    "Universty of Wisconsin Madison": "University of Wisconsin-Madison",
    "UW Madison": "University of Wisconsin-Madison",
    "UW-Madison": "University of Wisconsin-Madison",
}

"""
List of affiliations which are to be marked as Unknown
"""
UNKNOWN_AFFILIATIONS = ["", "-"]

UNKNOWN_AFFILIATION_WORD = "Unknown"

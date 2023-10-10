"""
question2.py - data manipulation

You are managing a cake baking competition.
There are three tables - red, green, and blue - each with five participants.
Everyone has baked a cake,
and has been asked to rate the other cakes on their table.

data.csv contains the ratings each participant gave to each other.

You are to implement a data processing pipeline

a) Complete the function load_reviews which takes a file path and returns
    a list of dictionaries with keys
        "id", "table", "reviewer", "baker", "score", "comment"

    e.g.
    [
        {"id": 1, "table": "blue", "reviewer": "Liam", "baker": "Amara", score: "2", comment: "I appreciate the creativity, but it didn't fully deliver."},
        {"id": 4, "table": "red", "reviewer": "James", "baker": "Sophia", score: "5", comment: "A true work of art that left everyone in awe."}
    ]

b) The function group_by_table should take the result from load_reviews and return
    a dictionary whose keys are the unique table names in the dataset (e.g. "red", "green", "blue")
    and values are lists containing each of the review lines for that table.

    e.g.
    {
        "blue" : [
            {"id": 1, "table": "blue", "reviewer": "Liam", "baker": "Amara", score: "2", comment: "I appreciate the creativity, but it didn't fully deliver."}
        ],
        "red" : [
            {"id": 4, "table": "red", "reviewer": "James", "baker": "Sophia", score: "5", comment: "A true work of art that left everyone in awe."}
        ]
    }

c) The function table_grids should take the output of group_by_table and
    return a nested dictionary where giving - in order - the table, the reviewer, and the baker
    will return the score that reviewer gave to that baker.
    i.e. if there is a line item in the dataset,
        {"id": 1, "table": "blue", "reviewer": "Liam", "baker": "Amara", score: "2", comment: "I appreciate the creativity, but it didn't fully deliver."}
    then,
        grid = table_grids(grouped_reviews)
        grid["blue"]["Liam"]["Amara"]
    will equal 2

TOTAL POINTS AVAILABLE: 5 

Code Functionality (5)
a) 2 POINTS
b) 1 POINT
c) 2 POINTS
"""

def load_reviews(file_path):
    return []

def group_by_table(reviews):
    return {}

def table_grids(grouped_reviews):
    return {}

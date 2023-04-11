#!/usr/bin/env python3
"""
This module contains the `top_students` function
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    args:
        mongo_colletion (Collection): pymongo collection object
    return
        (list): list of students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': "$topics.score"}
            }
        },
        {'$sort': {"averageScore": -1}}
    ])

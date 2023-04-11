#!/usr/bin/env python3
"""
This module contains the `insert_school` function
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    args:
        mongo_collection (Collaction): pymongo collection object
        kwargs (dict): key-value pair to add the document
    """
    if not mongo_collection or len(kwargs) == 0:
        return
    return mongo_collection.insert(kwargs)
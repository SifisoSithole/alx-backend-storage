#!/usr/bin/env python3
"""
This module contains the `update_topics`
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    args:
        mongo_collection (Collection): pymongo collection object
        name (str): will be the school name to update
        topics (list): list of topics approached in the school
    """
    if not mongo_collection or len(topics) == 0:
        return
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
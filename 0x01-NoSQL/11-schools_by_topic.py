#!/usr/bin/env python3
"""
This module contains the `schools_by_topic`
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of schools having a specific topic
    args:
        mongo_collection: pymongo collection object
        topic (str): topic searched
    return
        (list): school having a specific topic
    """
    return [school for school in mongo_collection.find({"topics": topic})]
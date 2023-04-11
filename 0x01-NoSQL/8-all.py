#!/usr/bin/env python3
"""
This module contains the `list_all` function
"""
from typing import List, Dict, Any


def list_all(mongo_collection) -> List[Dict[str, Any]]:
    """
    lists all documents in a collection

    args:
        mongo_collection (Collection): pymongo collection object
    return:
        (list): returns a list of all documents in a collection
    """

    if not mongo_collection:
        return []
    return list(mongo_collection.find())
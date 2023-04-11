#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    method_collection = client.logs.nginx

    print("{} logs".format(method_collection.estimated_document_count()))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = method_collection.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, method_count))

    get_status_doc = method_collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print("{} status check".format(get_status_doc))
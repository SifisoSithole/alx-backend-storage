#!/usr/bin/env python3
"""
This module contains the `Cache` class
"""
import redis
import uuid
from typing import Any


class Cache:
    """
    A class representing a cache for storing and retrieving data.

    Attributes:
        redis (Redis): A private variable that is an instance of Redis

    Methods:
        store(data): Store data in the cache with a generated key.
    """

    def __init__(self):
        """
        Initialize a new Cache object.
        """
        self._redis = redis.Redis()

    def store(self, data: Any) -> str:
        """
        Store data in the cache with a generated key

        args:
            data (Any): Data to store in cache

        return
            key (str): Key of the stored data
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

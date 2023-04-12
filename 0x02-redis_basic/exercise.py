#!/usr/bin/env python3
"""
This module contains the `Cache` class
"""
import redis
import uuid
from typing import Any, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts how many times methods of the Cache class are called

    args:
        method (Callable): called method
    return:
        (Callable): return function that increments the count
        for that key every time the method is called and returns
        the value returned by the original method
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """
    A class representing a cache for storing and retrieving data.

    Attributes:
        redis (Redis): A private variable that is an instance of Redis

    Methods:
        store(data): Stores data in the cache with a generated key.
        get(key, fn): Retrieve the value associated with a given key and
        convert to a desired format if fn is provided
    """

    def __init__(self):
        """
        Initialize a new Cache object.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    def get(self, key: str, fn: Callable[[bytes], Any] = None) -> Any:
        """
        Retrieve the value associated with a given key and
        convert to a desired format if fn is provided

        args:
            key (str): Key for the value to retreive
            fn (Callable): Function to convert the value to a desired format
        return:
            value (Any): Retreived value, converted to the desired format if
            fn was provided
        """
        if type(key) is not str:
            raise TypeError('key must be a string')
        value = self._redis.get(key)
        if not value:
            return value
        if fn:
            if not callable(fn):
                raise TypeError("fn must be a callable function")
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve the value associated with a given key and
        convert it to a string

        args:
           key (str): Key for the value to retreive

        return:
            (str): retreived value
        """
        if type(key) is not str:
            raise TypeError('key must be a string')
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Retrieve the value associated with a given key and
        convert it to an integer

        args:
           key (str): Key for the value to retreive

        return:
            (int): retreived value
        """
        if type(key) is not str:
            raise TypeError('key must be a string')
        return self.get(key, int)

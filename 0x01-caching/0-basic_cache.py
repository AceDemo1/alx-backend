#!/usr/bin/python3
"""Cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """define class"""
    def __init__(self):
        """initialize class"""
        super().__init__()

    def put(self, key, item):
        """put into cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get key value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]



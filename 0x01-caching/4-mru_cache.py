#!/usr/bin/env python3
"""Create MRU cache"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """define class"""

    def __init__(self):
        """initialize class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put into cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                key_discarded, _ = self.cache_data.popitem()
                print(f'DISCARD: {key_discarded}')
            self.cache_data[key] = item

    def get(self, key):
        """get value of key"""
        value = self.cache_data.pop(key) if key in self.cache_data else None
        if value:
            self.cache_data[key] = value
        return value

#!/usr/bin/env python3
"""Create LFU cache"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """define class 
    -----
    -----
    you dont need to use the pop method in both put and get method
    it will work regardless
    -----
    -----
    """

    def __init__(self):
        """initialize class"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frq_map = OrderedDict()

    def put(self, key, item):
        """put into cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
                self.frq_map[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_frq = min(self.frq_map.values())
                    for k, v in self. frq_map.items():
                        if v == min_frq:
                            min_key = k
                            break
                    self.cache_data.pop(min_key)
                    self.frq_map.pop(min_key)
                    print(f'DISCARD: {min_key}')
                self.frq_map[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """get value of key"""
        value = self.cache_data.pop(key) if key in self.cache_data else None
        if value:
            self.cache_data[key] = value
            self.frq_map[key] = self.frq_map.get(key, 0) + 1
        return value

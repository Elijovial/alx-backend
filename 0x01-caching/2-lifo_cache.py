#!/usr/bin/python3

"""
FIFO cache module
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Dict caching system
    """
    def __init__(self):
        """
        initialize
        """
        self.cache_data = {}
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    last_key = self.keys.pop()
                    del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)

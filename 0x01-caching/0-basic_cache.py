#!/usr/bin/env python3
from base_caching import BaseCaching
"""
A class BasicCache that inherits from BaseCaching and is a caching system
"""


class BasicCache(BaseCaching):
    """
    Dict caching system
    """
    def put(self, key, item):
        """
        Add an item to the cache.
        Args:
            key: The key for the cache entry.
            item: The value to be stored.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        Args:
            key: The key to look up in the cache.
        Returns:
            The value associated with the key, or None if not found.
        """
        return self.cache_data.get(key, None)

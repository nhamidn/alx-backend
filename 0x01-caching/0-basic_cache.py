#!/usr/bin/env python3
""" Basic-Cache module
"""



from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A simple caching system.
    """
    def put(self, key, item):
        """ Add an item in the cache data.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from cache data.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

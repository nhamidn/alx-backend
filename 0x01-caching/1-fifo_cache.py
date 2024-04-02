#!/usr/bin/env python3
""" Basic-Cache module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A simple FIFO caching system.
    """

    def __init__(self):
        """ Init method.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ Add an item in the cache data.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_key = self.key_order.pop(0)
                    del self.cache_data[discarded_key]
                    print("DISCARD: {}".format(discarded_key))
                self.cache_data[key] = item
                self.key_order.append(key)

    def get(self, key):
        """ Get an item by key from cache data.
        """
        return self.cache_data.get(key, None)

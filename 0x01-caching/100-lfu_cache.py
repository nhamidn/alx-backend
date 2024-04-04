#!/usr/bin/env python3
""" Basic-Cache module
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ A simple LFU caching system.
    """

    def __init__(self):
        """ Init method.
        """
        super().__init__()
        self.key_frequency = {}
        self.key_order = {}
        self.m_f = 1

    def put(self, key, item):
        """ Add an item in the cache data.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.get(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.update_cache()
        self.cache_data[key] = item
        self.key_frequency[key] = 1
        if 1 not in self.key_order:
            self.key_order[1] = []
        self.key_order[1].append(key)
        self.m_f = 1

    def get(self, key):
        """ Get an item by key from cache data.
        """
        if key is None or key not in self.cache_data:
            return None

        freq = self.key_frequency[key]
        self.key_frequency[key] += 1
        self.key_order[freq].remove(key)

        if not self.key_order[freq]:
            del self.key_order[freq]
            if freq == self.m_f:
                self.m_f += 1

        if freq + 1 not in self.key_order:
            self.key_order[freq + 1] = []
        self.key_order[freq + 1].append(key)

        return self.cache_data.get(key, None)

    def update_cache(self):
        """ Method that update the cache depeneding on frenquency.
        """
        while self.m_f not in self.key_order or not self.key_order[self.m_f]:
            self.m_f += 1

        d_key = self.key_order[self.m_f].pop(0)
        if not self.key_order[self.m_f]:
            del self.key_order[self.m_f]

        del self.cache_data[d_key]
        del self.key_frequency[d_key]
        print("DISCARD: {}".format(d_key))

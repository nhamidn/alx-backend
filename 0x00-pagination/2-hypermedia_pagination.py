#!/usr/bin/env python3
"""
2-hypermedia_pagination module.
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that return a range from a given page and size."""
    last_element = page * page_size
    first_element = last_element - page_size
    return (first_element, last_element)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function that get the content of a given pagination info.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page >= 0
        assert page_size > 0

        li = self.dataset()
        first, last = index_range(page, page_size)
        return li[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Function returns a dictionary containing key-value pairs.
        """
        data = self.get_page(page, page_size)
        first, last = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if last < len(self.__dataset) else None,
            'prev_page': page - 1 if first > 0 else None,
            'total_pages': total_pages
        }

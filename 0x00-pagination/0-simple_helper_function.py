#!/usr/bin/python3
"""
0-simple_helper_function module that defines a index_range function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that return a paginated pages range from a given page and size."""
    last_element = page * page_size
    first_element = last_element - page_size
    return (first_element, last_element)

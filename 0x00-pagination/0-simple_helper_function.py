#!/usr/bin/python3
"""
0-simple_helper_function module
"""


def index_range(page, page_size):
    """Function that return a paginated pages range"""
    last_element = page * page_size
    first_element = last_element - page_size
    return (first_element, last_element)

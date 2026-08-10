#!/usr/bin/env python3
"""
Helper function for pagination.
Returns a tuple (start_index, end_index)
based on page and page_size.
"""


def index_range(page, page_size):
    """
    Calculate start and end index for pagination.

    Args:
        page (int): page number (1-indexed)
        page_size (int): number of items per page

    Returns:
        tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

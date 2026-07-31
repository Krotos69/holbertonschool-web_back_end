#!/usr/bin/env python3
"""
Module for computing lengths of elements in an iterable of strings.
Provides element_length(lst) which returns a list of (string, length) tuples.
"""


from typing import Iterable, List, Tuple


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """
    Return a list of tuples containing each string and its length.

    Args:
        lst (Iterable[str]): Iterable of strings.

    Returns:
        List[Tuple[str, int]]: List of (string, length) tuples.
    """
    return [(i, len(i)) for i in lst]

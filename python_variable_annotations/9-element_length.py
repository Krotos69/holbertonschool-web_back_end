#!/usr/bin/env python3
"""
Module for computing lengths of elements in an iterable of sequences.
Provides element_length(lst) which returns a list of (sequence, length) tuples.
"""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each sequence and its length.

    Args:
        lst (Iterable[Sequence]): Iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: List of (sequence, length) tuples.
    """
    return [(i, len(i)) for i in lst]

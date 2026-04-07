#!/usr/bin/env python3
"""
Type‑annotated function element_length
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element in the iterable
    and its corresponding length.

    Args:
        lst: An iterable containing sequence-type elements.

    Returns:
        A list of tuples where each tuple contains:
        - the original element
        - the length of that element
    """
    return [(i, len(i)) for i in lst]

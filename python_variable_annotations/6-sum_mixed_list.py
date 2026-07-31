#!/usr/bin/env python3
"""
Module for summing a mixed list of ints and floats.
Provides sum_mixed_list(mxd_lst) which returns the total as a float.
"""


from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """
    Return the sum of a list containing ints and floats.

    Args:
        mxd_lst (List[float | int]): Mixed list of numbers.

    Returns:
        float: The sum of all values in mxd_lst.
    """
    return float(sum(mxd_lst))

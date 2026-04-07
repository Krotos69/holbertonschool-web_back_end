#!/usr/bin/env python3
"""type-annotated function sum_mixed_list which takes a list mxd_lst
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list containing intergers and floats
    """
    return float(sum(mxd_lst))

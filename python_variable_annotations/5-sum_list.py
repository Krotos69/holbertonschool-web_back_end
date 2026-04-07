#!/usr/bin/env python3
"""
type-annotatted function sum_list that takes a list input_list of
floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input: List[float]) -> float:
    """
    Returns the sum of a list of floats
    """
    return sum(input)

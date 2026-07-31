#!/usr/bin/env python3
"""
Module for summing a list of floats.
Provides sum_list(input_list) which returns the total as a float.
"""

def sum_list(input_list: list[float]) -> float:
    """
    Return the sum of a list of floats.

    Args:
        input_list (list[float]): List of floats to sum.

    Returns:
        float: The sum of all floats in input_list.
    """
    return sum(input_list)

#!/usr/bin/env python3
"""
Module for creating multiplier functions.
Provides make_multiplier(multiplier) which returns a function
that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The number used to multiply.

    Returns:
        Callable[[float], float]: A function that multiplies its argument.
    """
    def mult(value: float) -> float:
        return value * multiplier

    return mult

#!/usr/bin/env python3
"""
Module for creating a typed key/value tuple.
Provides to_kv(k, v) which returns (k, v squared as float).
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is the string k and the second
    element is the square of v as a float.

    Args:
        k (str): Key string.
        v (Union[int, float]): Number to square.

    Returns:
        Tuple[str, float]: (k, v squared as float).
    """
    return (k, float(v ** 2))

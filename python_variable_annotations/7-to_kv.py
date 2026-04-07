#!/usr/bin/env python3
"""Annotate the to_kv function's parameters and return values with the appropriate types."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int,float]) -> Tuple[str, float]:
    """Returns a tuple where:
    - the first element is the string k
    - the second element is the square of v as a float(string)
    """
    return (k, float(v **2))

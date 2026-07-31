#!/usr/bin/env python3
"""
Module for a typed floor function.
Provides floor(n) which returns the floor of a float.
"""

def floor(n: float) -> int:
    """
    Return the floor of a float.

    Args:
        n (float): Number to floor.

    Returns:
        int: The floor of n.
    """
    return int(n // 1)

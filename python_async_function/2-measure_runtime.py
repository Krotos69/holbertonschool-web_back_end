#!/usr/bin/env python3
"""
This module provides a function that measures the average runtime of executing
the wait_n coroutine. It calculates how long the coroutine takes to run for a
given number of iterations and returns the average time per execution.
"""

import asyncio
import time
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of the wait_n coroutine.

    The function runs wait_n(n, max_delay) and computes the total elapsed time.
    It then returns the average time per coroutine execution as a float.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay allowed for each coroutine.

    Returns:
        float: The average execution time per coroutine.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    return total_time / n

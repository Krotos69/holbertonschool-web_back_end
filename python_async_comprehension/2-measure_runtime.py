#!/usr/bin/env python3
"""
Alternate module that measures the runtime of executing multiple
asynchronous comprehensions in parallel.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel using a list
    comprehension to build the tasks, then return the total runtime.
    """
    start = time.perf_counter()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end = time.perf_counter()
    return end - start

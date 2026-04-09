#!/usr/bin/env python3
"""
Module for executing multiple asynchronous tasks using task_wait_random.

This module defines the coroutine task_wait_n, which schedules several
instances of task_wait_random concurrently and returns their results
in ascending order. It is used to demonstrate asynchronous task
management and concurrency in Python.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times concurrently and return the delays.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay allowed for each task.

    Returns:
        List[float]: A sorted list of all delays returned by the tasks.

    This coroutine creates n asyncio Tasks using task_wait_random,
    waits for all of them to complete, and returns their results
    sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

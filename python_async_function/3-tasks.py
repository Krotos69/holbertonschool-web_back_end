#!/usr/bin/env python3
"""
Module that provides a function to create an asyncio.Task
for executing wait_random asynchronously.
"""

import asyncio
from typing import Callable
wait_random: Callable = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs wait_random.

    Args:
        max_delay (int): Maximum delay passed to wait_random.

    Returns:
        asyncio.Task: A task wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))

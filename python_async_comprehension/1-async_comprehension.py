#!/usr/bin/env python3
"""
This module defines a coroutine that collects random numbers generated
asynchronously using an async comprehension.
"""

from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random floating-point numbers from the async_generator
    using an asynchronous comprehension and return them as a list.
    """
    return [value async for value in async_generator()]

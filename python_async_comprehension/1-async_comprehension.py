#!/usr/bin/env python3
"""
This module defines a coroutine that collects random numbers generated
asynchronously using an async comprehension.
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collect 10 random floating-point numbers from the async_generator
    using an asynchronous comprehension and return them as a list.
    """
    return [i async for i in async_generator()]

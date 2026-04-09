#!/usr/bin/env python3
"""
This module defines an asynchronous utility function that waits for a random
delay and returns the amount of time waited.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it.

    Args:
        max_delay: The maximum number of seconds to wait.

    Returns:
        The actual delay time as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

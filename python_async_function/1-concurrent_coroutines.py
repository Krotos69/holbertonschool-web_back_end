#!/user/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times and return delays in ascending order."""
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays =[]
    for task in asyncio.as_completed(task):
        delay = await task
        delays.append(delay)
        
    return delays

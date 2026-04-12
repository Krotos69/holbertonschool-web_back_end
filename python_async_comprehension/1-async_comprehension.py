#!/usr/bin/env python3
import asyncio
async_generator = __import__('0_async_generator').async_generator

async def async_comprehension():
    """Collect 10 random numbers from async_generator using async comprehension."""
    return [i async for i in async_generator()]

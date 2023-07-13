#!/usr/bin/env python3
"""asynch generator"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    results = [i async for i in async_generator()]
    return results

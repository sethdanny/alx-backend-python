#!/usr/bin/env python3
""" async module """


import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """wait for a random number for seconds"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay

#!/usr/bin/env python3
"""
Coroutine called async_generator that takes no arguments
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main():
    async for value in async_generator():
        print(value)


if __name__ == "__main__":
    asyncio.run(main())
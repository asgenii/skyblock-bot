import asyncio
import aiohttp
import time

last_request = 0

async def cooldown(url: str):
    global last_request

    wait = 10 - (time.time() - last_request)
    if wait > 0:
        await asyncio.sleep(wait)

    last_request = time.time()

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return await r.json()
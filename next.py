import asyncio
import json

import aiohttp


async def get_currency():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.exchangerate.host/latestbase=USD") as resp:
            print(await resp.text())
            json_obj = json.loads(str(await resp.text()))
            print(json_obj["rates"]["RUB"])


asyncio.run(get_currency())

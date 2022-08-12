from aiogram.dispatcher.filters.state import StatesGroup, State
import aiohttp
from config import API_TOKEN
import json


async def geocoding(city_name, country_code):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_TOKEN}') as resp:
            json_obj = json.loads(str(await resp.text()))
            return str(json_obj[0]["lon"]), str(json_obj[0]["lat"])


async def weatheer(name):
    lat, lon = await geocoding(name, "Russian Federation")
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_TOKEN}&units=metric') as resp:
            print(await resp.text())
            json_obj = json.loads(str(await resp.text()))
            return str(json_obj["main"]["temp"])

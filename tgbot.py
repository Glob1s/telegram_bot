from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext
import logging
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from name import weatheer
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)
@dp.message_handler()
async def weather(message: types.Message):
    s = message.text

    await message.reply(str(await weatheer(s)))
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

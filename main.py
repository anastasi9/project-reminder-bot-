import logging
import asyncio
import aiogram


from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message(message: types.Message):
    await message.answer("Привет! Я бот для заказа еды. Что бы Вы хотели заказать?")

@dp.message_handler(commands=['start'], content_types=types.ContentType.COMMAND)
async def start_command_handler(message: types.Message):

@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message(message: types.Message):
    await message.answer("Ваш заказ принят! Мы свяжемся с Вами в ближайшее время.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='6125622513:AAHEpaSqhAB7-sEUAtucoUA-sBfCYd6aRO4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello, I'm a bot!")

if __name__ == '__main__':
    executor.start_polling(dp, loop=asyncio.get_event_loop())





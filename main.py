from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor



TOKEN_API ="6125622513:AAHEpaSqhAB7-sEUAtucoUA-sBfCYd6aRO4"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message(message: types.Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



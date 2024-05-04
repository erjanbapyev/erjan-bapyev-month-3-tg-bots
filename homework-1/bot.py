from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart

from database import create_table, add_user

bot = Bot(token='YOUR_TOKEN')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    await add_user(user_id, username)
    await message.answer("Привет! Теперь вы зарегистрированы в нашей системе.")

async def start_bot():
    await create_table()
    await dp.start_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(start_bot())

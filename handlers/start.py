import sqlite3

from aiogram import Router, types
from aiogram.filters import Command

from config import bot, ADMIN_ID, MEDIA_PATH
from const import START_MENU_TEXT
from database import sql_queries
from database.a_db import AsyncDatabase
from keyboards.start import start_menu_keyboard

router = Router()


@router.message(Command("start"))
async def start_menu(message: types.Message,
                     db=AsyncDatabase()):
    print(message)
    await db.execute_query(
        query=sql_queries.INSERT_USER_QUERY,
        params=(
            None,
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name
        ),
        fetch='none'
    )
    animation_file = types.FSInputFile(MEDIA_PATH + "bot-ani.gif")
    await bot.send_animation(
        chat_id=message.from_user.id,
        animation=animation_file,
        caption=START_MENU_TEXT.format(
            user=message.from_user.first_name
        ),
        reply_markup=await start_menu_keyboard()
    )


@router.message(lambda message: message.text == "dorei")
async def admin_start_menu(message: types.Message,
                           db=AsyncDatabase()):
    if int(ADMIN_ID) == message.from_user.id:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Here is ur Admin page"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="U have not access!!! 😡"
        )
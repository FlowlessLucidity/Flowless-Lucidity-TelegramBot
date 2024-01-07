import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

import buttons
import keyboards
from database import Database
from secrets import *


dp = Dispatcher()
database = Database()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    print(message.from_user.id)
    if message.from_user.id in TRUSTED_USERS:
        await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=keyboards.main_keyboard)
    else:
        await message.answer("Незваный гость, обратитесь к создателю, чтобы начать.")

@dp.message()
async def command_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    if message.from_user.id in TRUSTED_USERS:
        command = message.text
        match command:
            case buttons.new_dream.text:
                await message.answer(buttons.new_dream.text)
            case buttons.random_dream.text:
                record = asyncio.get_event_loop().create_task(database.random_dream())
                await message.answer(record["dream"])
            case _:
                await message.answer("Пока не имплементировано")
    else:
        await message.answer("Незваный гость, обратитесь к создателю, чтобы начать.")



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
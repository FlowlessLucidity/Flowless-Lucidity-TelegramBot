import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from database import Database
from handlers import basic_handlers, not_trusted, new_dream_handler
from secrets import *


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    database = Database()
    dp = Dispatcher()
    dp.include_routers(basic_handlers.router, new_dream_handler.router, not_trusted.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, db=database)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())

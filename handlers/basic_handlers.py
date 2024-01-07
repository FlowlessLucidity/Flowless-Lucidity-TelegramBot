from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from motor.core import AgnosticDatabase as MDB

from filters.trust_list import TrustedFilter, NotTrustedFilter
from keyboards import buttons
from keyboards.mainboard import main_keyboard
from secrets import *


router = Router()
router.message.filter(TrustedFilter())
@router.message(
    CommandStart(),
    TrustedFilter())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    print(message.from_user.id)
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!", reply_markup=main_keyboard)

@router.message(
    TrustedFilter(),
    F.text == buttons.new_dream.text)
async def new_dream_handler(message: Message, db: MDB) -> None:
    await message.answer(buttons.new_dream.text)

@router.message(

    F.text == buttons.random_dream.text)
async def new_dream_handler(message: Message, db: MDB) -> None:
    record = await db.get_random_dream()
    await message.answer(record["dream"])

@router.message(TrustedFilter())
async def new_dream_handler(message: Message, db: MDB) -> None:
    await message.answer("Пока не имплементировано")

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from motor.core import AgnosticDatabase as MDB

import keyboards.dateboard
from filters.trust_list import TrustedFilter
from keyboards import buttons
from keyboards.mainboard import main_keyboard
from secrets import *
from utils.states import NewDreamState

router = Router()
router.message.filter(TrustedFilter())
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    print(message.from_user.id)
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!", reply_markup=main_keyboard)

@router.message(F.text == buttons.new_dream.text)
async def new_dream_handler(message: Message, db: MDB, state: FSMContext) -> None:
    await message.answer(
        text="Введите дату",
        reply_markup=keyboards.dateboard.today_or_diff
    )
    await state.set_state(NewDreamState.enter_date)


@router.message(F.text == buttons.random_dream.text)
async def random_dream_handler(message: Message, db: MDB) -> None:
    record = await db.get_random_dream()
    answer_text = ''
    answer_form = {
        'date': '📅 ',
        'sleep type': '🌙 ' if record['sleep type'] == 'Дневной' else "☀️ ",
        'dream': '',
        'dream type': '🌙' ,
        'location': '🌄 ',
    }
    for key in answer_form.keys():
        if record[key] is not None:
            answer_text += f'{answer_form[key]}{record[key]}\n'
    await message.answer(answer_text)



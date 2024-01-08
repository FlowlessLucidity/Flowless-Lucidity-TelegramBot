import datetime

import pytz
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from motor.core import AgnosticDatabase as MDB

import keyboards.mainboard
from filters.trust_list import TrustedFilter
from keyboards import buttons
from keyboards.mainboard import main_keyboard
from secrets import *
from utils.states import NewDreamState

router = Router()
router.message.filter(TrustedFilter())

@router.message(NewDreamState.enter_date)
async def date_handler(message: Message, state: FSMContext) -> None:
    match message.text:
        case buttons.today_date.text:
            await state.update_data(date=datetime.datetime.utcnow())
            await state.set_state(NewDreamState.enter_dream)
            await message.answer("Теперь сам сон")
        case buttons.diff_date.text:
            try:
                sussy_date = datetime.datetime.strptime(message.text, "%d.%m.%y")
                await state.update_data(date=sussy_date)
                await state.set_state(NewDreamState.enter_dream)
                await message.answer("Теперь сам сон")
            except ValueError:
                await message.answer("Ещё раз, dd.mm.yy")
@router.message(NewDreamState.enter_dream)
async def dream_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(dream=message.text.strip())
    data = await state.get_data()
    await state.set_state(NewDreamState.confirm)
    await message.answer("Нормально?\n"+str(data), reply_markup=keyboards.mainboard.yes_no)
@router.message(NewDreamState.confirm, F.text.lower()=='да')
async def dream_handler(message: Message, state: FSMContext, db: MDB) -> None:
    data = await state.get_data()
    await db.set_new_dream(data)
    await message.answer("Добавлено", reply_markup=keyboards.mainboard.main_keyboard)
    await state.clear()

@router.message(NewDreamState.confirm, F.text.lower()=='нет')
async def dream_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text="Ещё раз", reply_markup=keyboards.dateboard.today_or_diff)
    await state.set_state(NewDreamState.enter_date)

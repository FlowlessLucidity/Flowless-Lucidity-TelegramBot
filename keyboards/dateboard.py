from aiogram.types import ReplyKeyboardMarkup

from keyboards import buttons

today_or_diff = ReplyKeyboardMarkup(
    keyboard=[
        [
            buttons.diff_date,
            buttons.today_date,
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
from aiogram.types import(
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import buttons


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            buttons.update_dream,
            buttons.random_dream,
        ],
        [
            buttons.list_dreams,
        ],
        [
            buttons.new_dream
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
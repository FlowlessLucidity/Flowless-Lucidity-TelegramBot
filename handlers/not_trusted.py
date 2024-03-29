from aiogram import Router
from aiogram.types import Message
from filters.trust_list import  NotTrustedFilter

router = Router()
router.message.filter()

@router.message(NotTrustedFilter())
async def for_unauthorized(message: Message) -> None:
    await message.answer("Незваный гость, обратитесь к создателю, чтобы начать.")

@router.message()
async def unknown_handler(message: Message) -> None:
    await message.answer("Пока не имплементировано")

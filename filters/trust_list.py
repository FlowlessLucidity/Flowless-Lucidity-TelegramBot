from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

from secrets import *


class TrustedFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:  # [3]
        return message.from_user.id in TRUSTED_USERS

class NotTrustedFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:  # [3]
        return message.from_user.id not in TRUSTED_USERS

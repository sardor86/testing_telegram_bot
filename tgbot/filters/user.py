import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.models import Users


class UserFilter(BoundFilter):
    key = 'register'

    def __init__(self, register: typing.Optional[bool]):
        self.register = register

    async def check(self, obj):
        return await Users().check_user(obj.from_user.id) == self.register

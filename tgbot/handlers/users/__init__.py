from aiogram import Dispatcher

from .user import register_user
from .register import register_register_handler


def register_all_user_handlers(dp: Dispatcher):
    register_register_handler(dp)
    register_user(dp)

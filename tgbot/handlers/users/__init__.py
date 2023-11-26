from aiogram import Dispatcher

from .user import register_user
from .register import register_register_handler
from .take_test import register_take_test


def register_all_user_handlers(dp: Dispatcher):
    register_register_handler(dp)
    register_user(dp)
    register_take_test(dp)

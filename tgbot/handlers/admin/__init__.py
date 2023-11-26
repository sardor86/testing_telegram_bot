from aiogram import Dispatcher

from tgbot.handlers.admin.menu import register_admin
from tgbot.handlers.admin.create_test import register_create_new_test_handler
from tgbot.handlers.admin.delete_test import register_delete_test_handler


def register_admin_handlers(dp: Dispatcher):
    register_admin(dp)
    register_create_new_test_handler(dp)
    register_delete_test_handler(dp)

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.config import logger
import logging

from tgbot.keyboards import admin_menu_keyboard


async def admin_menu(message: Message):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Admin menu')
    await message.reply("Hello, admin!", reply_markup=admin_menu_keyboard())


def register_admin(dp: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Register admin handler')
    dp.register_message_handler(admin_menu, commands=['admin_menu'], is_admin=True)

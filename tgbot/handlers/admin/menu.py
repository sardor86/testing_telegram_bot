from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.config import logger
import logging

from tgbot.keyboards import admin_menu_keyboard
from tgbot.models import Tests, TempKey


async def admin_menu(message: Message):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Admin menu')
    await message.reply("Hello, admin!", reply_markup=await (admin_menu_keyboard()))


async def get_all_test(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get test list')
    tests_list = await Tests().get_all_tests()
    answer = ''

    for test in tests_list:
        answer += f'{test.name}\n'

    logger.info('send answer')
    await callback.message.edit_text(answer)


async def create_new_key(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('create new key')
    new_key = await TempKey().create_key()

    await callback.message.edit_text(f'Новый ключ: {new_key}')


def register_admin(dp: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Register admin menu handler')
    dp.register_message_handler(admin_menu, commands=['admin_menu'], is_admin=True)

    logger.info('Register get all test handler from admin')
    dp.register_callback_query_handler(get_all_test,
                                       lambda callback: callback.data == 'get_all_test',
                                       is_admin=True)

    logger.info('Register create new key handler from admin')
    dp.register_callback_query_handler(create_new_key,
                                       lambda callback: callback.data == 'create_temp_key',
                                       is_admin=True)

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import Dispatcher, FSMContext

from tgbot.config import logger
import logging

from tgbot.misc import RegisterUser
from tgbot.models import TempKey, Users


async def register_user(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    await callback.message.edit_text('Отправте ключ')

    logger.info('Set get key in RegisterUser')
    await RegisterUser.get_key.set()


async def get_key(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('check key')
    if await TempKey().check_key(message.text):
        logger.info('create user')
        await Users().add_user(message.from_user.id)

        logger.info('delete key')
        await TempKey().delete_key(message.text)

        await message.reply('Вы успешно зарегестрированы')

        logger.info('finish state')
        await state.finish()
        return

    logger.warning('Incorrect key')
    await message.reply('Неправильный ключ')


def register_register_handler(dp: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register register handler')
    dp.register_callback_query_handler(register_user,
                                       lambda callback: callback.data == 'user_register')

    logger.info('register get key handler')
    dp.register_message_handler(get_key,
                                state=RegisterUser.get_key,
                                register=False)

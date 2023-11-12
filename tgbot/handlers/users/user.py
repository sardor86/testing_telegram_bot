import logging

from aiogram.types import Message
from aiogram.dispatcher import Dispatcher, FSMContext

from tgbot.config import logger


async def cansel(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Command cancel')

    if not await state.get_state() is None:
        await message.reply('Отменено')
        await state.finish()


async def user_start(message: Message):
    await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start'])
    dp.register_message_handler(cansel, commands=['cansel'], state="*")

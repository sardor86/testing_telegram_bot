import logging

from aiogram.types import Message
from aiogram.dispatcher import Dispatcher, FSMContext

from tgbot.config import logger
from tgbot.keyboards import user_registration_menu, user_menu


async def cansel(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Command cancel')

    if not await state.get_state() is None:
        await message.reply('Отменено')
        await state.finish()


async def not_register(message: Message):
    await message.reply('Вы не зарегестрированы', reply_markup=(await user_registration_menu()))


async def user(message: Message):
    await message.reply('Пройти тест', reply_markup=await user_menu())


def register_user(dp: Dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register check user handler')
    dp.register_message_handler(not_register, register=False)

    logger.info('register cansel command handler')
    dp.register_message_handler(cansel, commands=['cansel'], state="*")

    logger.info('register user menu handler')
    dp.register_message_handler(user, commands=['menu'], register=True)

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import Dispatcher, FSMContext

import logging
from tgbot.config import logger

from tgbot.misc import DeleteTest
from tgbot.models import Tests


async def delete_test(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get all test')
    tests_list = await Tests().get_all_tests()
    answer = ''
    for test in tests_list:
        answer += f'{test.name}\n'

    await callback.message.edit_text(answer)
    await callback.message.reply('Напишите название теста\nВы в любое время можене отменить командой /cansel')

    logger.info('set get_name in DeleteTest state')
    await DeleteTest.get_name.set()


async def get_test(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('state finish')
    await state.finish()

    logger.info('get test')

    logger.info('delete questions')
    if await Tests().delete_test(message.text):
        logger.info('delete test')
        await message.reply('Тест удален')
        return

    logger.warning('test not found')
    await message.reply('Тест не найден')


def register_delete_test_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Register delete test handler')
    dp.register_callback_query_handler(delete_test,
                                       lambda callback: callback.data == 'delete_test',
                                       is_admin=True)

    logger.info('Register get test handler')
    dp.register_message_handler(get_test,
                                state=DeleteTest.get_name,
                                is_admin=True)

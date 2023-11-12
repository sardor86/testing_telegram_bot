from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext, Dispatcher

import logging
from tgbot.config import logger, path
import datetime

from tgbot.models import Tests
from tgbot.misc import AddNewTest


async def create_new_test(callback: CallbackQuery) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('create new test')
    await callback.message.edit_text('Отправьте файл с тестом')

    logger.info('set get_file in AddNewTest state')
    await AddNewTest.get_file.set()


async def get_file(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('state is finished')
    await state.finish()

    file = await message.bot.get_file(message.document.file_id)

    if not file.file_path.split('.')[-1] == 'xlsx':
        logger.WARNING('file format is incorrect')
        await message.reply('Файл с неправильным форматом')
        return

    logger.info('Download file')
    file_path = path / 'tests' / datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S-%f.xlsx')
    await message.bot.download_file(file.file_path, str(file_path))

    logger.info('Create data in data base')
    await Tests().create_test(file_path)


def register_create_new_test_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Register create new test handler')
    dp.register_callback_query_handler(create_new_test,
                                       lambda callback: callback.data == 'create_new_test',
                                       is_admin=True)
    logger.info('Register get file state in create new test handler')
    dp.register_message_handler(get_file,
                                is_admin=True,
                                content_types=['document'],
                                state=AddNewTest.get_file)

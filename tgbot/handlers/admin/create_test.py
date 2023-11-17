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
    await callback.message.edit_text('Отправьте название теста\nВы в любое время можене отменить командой /cansel')

    logger.info('set get_name in AddNewTest state')
    await AddNewTest.get_name.set()


async def get_name(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('check text')
    if await Tests().check_test(message.text):
        await message.reply('Такой тест уже существует')
        return

    logger.info('get tests name ant save it on RAM')
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('Отправьте нам файл с тестом')

    logger.info('set get_file in AddNewTest state')
    await AddNewTest.get_file.set()


async def get_file(message: Message, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    async with state.proxy() as data:
        test_name = data['name']

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
    test = await Tests().create_test(test_name)

    await message.reply('Тест был создан')


async def get_not_file(message: Message) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.warning('this is not file')
    await message.reply('Это не файл')


def register_create_new_test_handler(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Register create new test handler')
    dp.register_callback_query_handler(create_new_test,
                                       lambda callback: callback.data == 'create_new_test',
                                       is_admin=True)

    logger.info('Register get_name state in create new test handler')
    dp.register_message_handler(get_name,
                                is_admin=True,
                                content_types=['text'],
                                state=AddNewTest.get_name)

    logger.info('Register get_file state in create new test handler')
    dp.register_message_handler(get_file,
                                is_admin=True,
                                content_types=['document'],
                                state=AddNewTest.get_file)

    logger.info('Register get_not_file state in create new test handler')
    dp.register_message_handler(get_not_file,
                                lambda message: not message.document,
                                is_admin=True,
                                state=AddNewTest.get_file)

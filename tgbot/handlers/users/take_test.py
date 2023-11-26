from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import CallbackQuery

from tgbot.models import Tests, Questions

from tgbot.misc import TakeTest
from tgbot.keyboards import user_choice_test, user_start_take_test, user_test_answer
from tgbot.config import logger

import logging
import random


async def take_test(callback: CallbackQuery):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get all test')
    data_list = [[test.name, f'take_test:{test.name}'] for test in await Tests().get_all_tests()]
    await callback.message.edit_text('Выберите тест\n'
                                     'Чтобы отменить напешите /cansel', reply_markup=await user_choice_test(data_list))

    logger.info('set choice state in TakeTest')
    await TakeTest.choice.set()


async def get_test_name(callback: CallbackQuery, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('save test name in RAM')
    async with state.proxy() as data:
        data['test_name'] = callback.data.split(':')[-1]
        data['test_number'] = 0
        data['questions'] = await Questions().get_question((await Tests().get_test(data['test_name'])).id)
        data['question_len'] = len(data['questions'])
        data['correct_answer'] = None
        data['quantity_correct_answer'] = 0
        data['quantity_uncorrected_answer'] = 0

    logger.info('set passing state in TakeTest')
    await TakeTest.passing.set()

    await callback.message.edit_text('Начать тест', reply_markup=await user_start_take_test())


async def passing_test(callback: CallbackQuery, state: FSMContext) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('get data from RAM')
    async with state.proxy() as data:
        logger.info('check answer')
        if not data['correct_answer'] is None:
            if callback.data.split('_')[-1] == data['correct_answer']:
                data['quantity_correct_answer'] += 1
                await callback.message.edit_text('Правильный ответ')
            else:
                data['quantity_uncorrected_answer'] += 1
                await callback.message.edit_text('не правильный ответ')

        logger.info('check test_number')
        if data['test_number'] == data['question_len']:
            logger.info('get and send results')
            await callback.message.reply(f'Правильных ответов: {data["quantity_correct_answer"]}\n'
                                         f'Неправильных ответов: {data["quantity_uncorrected_answer"]}')

            logger.info('state is finishing')
            await state.finish()
            return

        logger.info('get questions')
        question: Questions.QuestionsTable = data["questions"][data["test_number"]]

        logger.info('create answers')
        answers = [question.correct_answer,
                   question.answer1,
                   question.answer2,
                   question.answer3]

        logger.info('shuffle answers')
        random.shuffle(answers)
        data['correct_answer'] = ['A', 'B', 'C', 'D'][answers.index(question.correct_answer)]

        await callback.message.reply(f'Вопрос: {question.question}\n'
                                     f'A: {answers[0]}\n'
                                     f'B: {answers[1]}\n'
                                     f'C: {answers[2]}\n'
                                     f'D: {answers[3]}\n',
                                     reply_markup=await user_test_answer())
        data['test_number'] += 1


def register_take_test(dp: Dispatcher) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('register take test handler')
    dp.register_callback_query_handler(take_test,
                                       lambda callback: callback.data == 'take_test',
                                       register=True)

    logger.info('register get test name handler')
    dp.register_callback_query_handler(get_test_name,
                                       state=TakeTest.choice)

    logger.info('register passing test handler')
    dp.register_callback_query_handler(passing_test,
                                       state=TakeTest.passing)

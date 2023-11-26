from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def admin_menu_keyboard() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup()

    inline_keyboard.add(InlineKeyboardButton('Создать тест', callback_data='create_new_test'))
    inline_keyboard.add(InlineKeyboardButton('Получить список тестов', callback_data='get_all_test'))
    inline_keyboard.add(InlineKeyboardButton('Удалить тест', callback_data='delete_test'))
    inline_keyboard.add(InlineKeyboardButton('Создать ключ', callback_data='create_temp_key'))

    return inline_keyboard


async def user_registration_menu() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup()

    inline_keyboard.add(InlineKeyboardButton('Зарегистрироватся', callback_data='user_register'))

    return inline_keyboard


async def user_menu() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup()

    inline_keyboard.add(InlineKeyboardButton('Пройти тест', callback_data='take_test'))

    return inline_keyboard


async def user_choice_test(data_list: list) -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup()

    for data in data_list:
        inline_keyboard.add(InlineKeyboardButton(data[0], callback_data=data[1]))

    return inline_keyboard


async def user_start_take_test() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup()

    inline_keyboard.add(InlineKeyboardButton('Начать', callback_data='user_start_take_test'))

    return inline_keyboard


async def user_test_answer() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup()

    inline_keyboard.add(InlineKeyboardButton('A', callback_data='answer_A'))
    inline_keyboard.add(InlineKeyboardButton('B', callback_data='answer_B'))
    inline_keyboard.add(InlineKeyboardButton('C', callback_data='answer_C'))
    inline_keyboard.add(InlineKeyboardButton('D', callback_data='answer_D'))

    return inline_keyboard

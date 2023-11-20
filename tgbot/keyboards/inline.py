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

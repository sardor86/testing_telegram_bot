from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def admin_menu_keyboard() -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup()

    inline_keyboard.add(InlineKeyboardButton('Создать тест', callback_data='create_new_test'))
    inline_keyboard.add(InlineKeyboardButton('Получить список тестов', callback_data='get_all_test'))
    inline_keyboard.add(InlineKeyboardButton('Удалить тест', callback_data='delete_test'))

    return inline_keyboard

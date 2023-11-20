from aiogram.dispatcher.filters.state import StatesGroup, State


class AddNewTest(StatesGroup):
    get_name = State()
    get_file = State()


class DeleteTest(StatesGroup):
    get_name = State()


class RegisterUser(StatesGroup):
    get_key = State()

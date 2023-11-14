from aiogram.dispatcher.filters.state import StatesGroup, State


class AddNewTest(StatesGroup):
    get_name = State()
    get_file = State()

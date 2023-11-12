from aiogram.dispatcher.filters.state import StatesGroup, State


class AddNewTest(StatesGroup):
    get_file = State()

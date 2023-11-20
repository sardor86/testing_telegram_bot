from .admin import AdminFilter
from .user import UserFilter


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(UserFilter)

from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class DataBase:
    host: str
    port: int
    user: str
    password: str
    db: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str('BOT_TOKEN'),
            admin_id=env.int('ADMIN')
        ),
        db=DataBase(
            host=env.str('DB_HOST'),
            port=env.int('DB_PORT'),
            user=env.str('DB_USER'),
            password=env.str('DB_PASS'),
            db=env.str('DB_NAME')
        )
    )

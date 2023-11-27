from dataclasses import dataclass

from environs import Env
from gino import Gino
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
gino_db = Gino()
path = Path(__file__).parent.parent


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class DataBase:
    host: str
    user: str
    password: str
    db: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase


async def set_gino(data_base: DataBase) -> None:
    await gino_db.set_bind(f'postgresql://{data_base.user}:'
                           f'{data_base.password}@'
                           f'{data_base.host}:5432/'
                           f'{data_base.db}')


async def load_config(path: str = None) -> Config:
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Get config')

    env = Env()
    env.read_env(path)

    config: Config = Config(
                            tg_bot=TgBot(
                                token=env.str('BOT_TOKEN'),
                                admin_id=env.int('ADMIN')
                            ),
                            db=DataBase(
                                host=env.str('DB_HOST'),
                                user=env.str('POSTGRES_USER'),
                                password=env.str('POSTGRES_PASSWORD'),
                                db=env.str('POSTGRES_DB')
                            )
                        )
    await set_gino(config.db)
    return config

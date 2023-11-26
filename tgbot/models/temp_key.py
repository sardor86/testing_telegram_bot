from tgbot.config import gino_db
from .base import Base

import random
import string


class TempKey(Base):
    class TempKeyTable(gino_db.Model):
        __tablename__ = 'temp_key'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        key = gino_db.Column(gino_db.String(25), nullable=False)

        def __str__(self) -> str:
            return f'<Key {self.id}>'

        def __repr__(self) -> str:
            return f'<Key {self.id}>'

    async def create_key(self) -> str:
        key = self.TempKeyTable(
            key=''.join([random.choice(string.ascii_letters) for _ in range(25)])
        )
        await key.create()
        return key.key

    async def check_key(self, key: str) -> bool:
        return not await self.TempKeyTable.query.where(self.TempKeyTable.key == key).gino.first() is None

    async def delete_key(self, key: str) -> bool:
        if await self.check_key(key):
            key = await self.TempKeyTable.query.where(self.TempKeyTable.key == key).gino.first()
            await key.delete()
            return True
        return False

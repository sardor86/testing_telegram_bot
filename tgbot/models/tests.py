from tgbot.config import gino_db
from .base import Base

import os


class Tests(Base):
    class TestTable(gino_db.Model):
        __tablename__ = 'tests'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        name = gino_db.Column(gino_db.String(50), nullable=False)
        path = gino_db.Column(gino_db.String(255), nullable=False)

        def __str__(self) -> str:
            return f'<Tests {self.id}>'

        def __repr__(self) -> str:
            return f'<Tests {self.id}>'

    async def create_test(self, name: str, path: str) -> int:
        test = self.TestTable(
            name=name,
            path=path
        )
        await test.create()
        return test.id

    async def check_test(self, test_name: str) -> bool:
        return not await self.TestTable.query.where(self.TestTable.name == test_name).gino.first() is None

    async def delete_test(self, test_name: str) -> bool:
        if await self.check_test(test_name):
            test = await self.TestTable.query.where(self.TestTable.name == test_name).gino.first()
            os.remove(test.path)
            await test.delete()
            return True
        return False

    async def get_all_tests(self) -> list:
        return await self.TestTable.query.gino.all()

    async def get_test(self, test_name: int) -> TestTable:
        return self.TestTable.query.where(self.TestTable.name == test_name).gino.first()

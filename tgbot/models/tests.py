from tgbot.config import gino_db
from .base import Base


class Tests(Base):
    class TestTable(gino_db.Model):
        __tablename__ = 'tests'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        path = gino_db.Column(gino_db.String(255), nullable=False)

        def __str__(self) -> str:
            return f'<Tests {self.id}>'

        def __repr__(self) -> str:
            return f'<Tests {self.id}>'

    async def create_test(self, img: str) -> int:
        event = self.TestTable(path=img)
        await event.create()

        return event.id

    async def check_test(self, test_id: int) -> bool:
        return not await self.TestTable.query.where(self.TestTable.id == test_id).gino.first() is None

    async def delete_event(self, test_id: int) -> bool:
        if await self.check_test(test_id):
            test = await self.TestTable.query.where(self.TestTable.id == test_id).gino.first()
            await test.delete()
            return True
        return False

    async def get_all_event(self) -> list:
        return await self.TestTable.query.gino.all()

    async def get_event(self, test_id: int) -> TestTable:
        return self.TestTable.query.where(self.TestTable.id == test_id).gino.first()

from tgbot.config import gino_db
from .base import Base


class Users(Base):
    class UserTable(gino_db.Model):
        __tablename__ = 'users'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        user_id = gino_db.Column(gino_db.Integer(), nullable=False)

        def __str__(self) -> str:
            return f'<Tests {self.id}>'

        def __repr__(self) -> str:
            return f'<Tests {self.id}>'

    async def add_user(self, user_id: int) -> int:
        user = self.UserTable(
            name=user_id
        )
        await user.create()
        return user.id

    async def check_user(self, user_id: int) -> bool:
        return not await self.UserTable.query.where(self.UserTable.user_id == user_id).gino.first() is None

    async def delete_test(self, user_id: int) -> bool:
        if await self.check_user(user_id):
            user = await self.UserTable.query.where(self.UserTable.user_id == user_id).gino.first()
            await user.delete()
            return True
        return False

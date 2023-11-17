from tgbot.config import gino_db
from .base import Base
from .tests import Tests


class Questions(Base):
    class QuestionsTable(gino_db.Model):
        __tablename__ = 'questions'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        test_name = gino_db.Column(gino_db.ForeignKey('tests.name'), nullable=False)
        question = gino_db.Column(gino_db.String(512), nullable=False)
        correct_answer = gino_db.Column(gino_db.String(512), nullable=False)
        answer1 = gino_db.Column(gino_db.String(512), nullable=False)
        answer2 = gino_db.Column(gino_db.String(512), nullable=False)
        answer3 = gino_db.Column(gino_db.String(512), nullable=False)

        def __str__(self) -> str:
            return f'<Questions {self.id}>'

        def __repr__(self) -> str:
            return f'<Questions {self.id}>'

    async def create_question(self, test: Tests.TestTable, data_list: list) -> None:
        for data in data_list:
            question = self.QuestionsTable(test_name=test.name,
                                           question=data['question'],
                                           correct_answer=data['correct_answer'],
                                           answer1=data['answer1'],
                                           answer2=data['answer2'],
                                           answer3=data['answer3'])
            await question.create()

    async def check_question(self, test: Tests.TestTable) -> bool:
        result = self.QuestionsTable.query.where(self.QuestionsTable.test_name == test.name).gino.first() is None
        return not result

    async def delete_question(self, test: Tests.TestTable) -> bool:
        if await self.check_question(test):
            question = await self.QuestionsTable.query.where(self.QuestionsTable.test_name == test.name).gino.first()
            await question.delete()
            return True
        return False

    async def get_all_questions(self) -> list:
        return await self.QuestionsTable.query.gino.all()

    async def get_question(self, test: Tests.TestTable) -> QuestionsTable:
        return self.QuestionsTable.query.where(self.QuestionsTable.test_name == test.name).gino.first()
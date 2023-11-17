import openpyxl
from pathlib import Path


class XlsxReader:
    def __init__(self, path: Path):
        self.workbook = openpyxl.load_workbook(path)
        self.worksheet = self.workbook.active

        self.row_size = self.worksheet.max_row

    def read(self) -> list:
        result = []

        for row in self.row_size:
            data = {
                'question': self.worksheet.cell(row=row, column=1),
                'correct_answer': self.worksheet.cell(row=row, column=2),
                'answer1': self.worksheet.cell(row=row, column=3),
                'answer2': self.worksheet.cell(row=row, column=4),
                'answer3': self.worksheet.cell(row=row, column=5),
            }
            result.append(data)

        return result

from typing import List
from student_class import Student

class Class:
    def __init__(self, name: str, class_num: int):
        self.name = name
        self.class_num = class_num
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def get_students(self) -> List[Student]:
        return self.students

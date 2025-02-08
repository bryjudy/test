class Class:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students(self):
        for student in self.students:
            print(student)
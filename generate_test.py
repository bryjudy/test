from class_class import Class
from student_class import Student

class1 = Class("Class 1")
class2 = Class("Class 2")

students = []
for i in range(10):
    student = Student(f"Student {i+1}")
    students.append(student)

for i in range(5):
    class1.add_student(students[i])

for i in range(5, 10):
    class2.add_student(students[i])

class1.print_students()
class2.print_students()
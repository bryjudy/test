from class_class import Class
from student_class import Student

class1 = Class("Class 1")
class2 = Class("Class 2")

students = []
for i in range(10):
    student = Student(age=20, birthday="2000-01-01")
    students.append(student)

class1.add_students(students[:5])
class2.add_students(students[5:])

class1.print_students()
class2.print_students()
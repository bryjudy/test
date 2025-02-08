import random
from student_class import Student
from class_class import Class

# Generate 10 random students
students = []
for _ in range(10):
    student = Student(age=random.randint(18, 25), birthday="01/01/2000")
    students.append(student)

# Generate 2 random classes
class1 = Class(name="Class1", class_num=1)
class2 = Class(name="Class2", class_num=2)

# Randomly assign students to classes
for student in students:
    if random.choice([True, False]):
        class1.add_student(student)
    else:
        class2.add_student(student)

# Print classes and students within the classes
print(f"{class1.name} (Class {class1.class_num}):")
for student in class1.students:
    print(f"Student - Age: {student.age}, Birthday: {student.birthday}")

print(f"\n{class2.name} (Class {class2.class_num}):")
for student in class2.students:
    print(f"Student - Age: {student.age}, Birthday: {student.birthday}")

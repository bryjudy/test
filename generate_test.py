import random
from student_class import Student
from class_class import Class

# Create 10 random students
students = []
for i in range(10):
    student = Student(age=random.randint(18, 25), birthday="01/01/2000")
    students.append(student)

# Create two random classes
class1 = Class(name="Class A", students=[])
class2 = Class(name="Class B", students=[])

# Randomly assign students to classes
for student in students:
    if random.choice([True, False]):
        class1.students.append(student)
    else:
        class2.students.append(student)

# Print classes and students within the classes
print(f"{class1.name}:")
for student in class1.students:
    print(f"Student - Age: {student.age}, Birthday: {student.birthday}")

print(f"\n{class2.name}:")
for student in class2.students:
    print(f"Student - Age: {student.age}, Birthday: {student.birthday}")

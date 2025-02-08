import random
from student_class import Student
from class_class import Class

# Parameters needed to create an instance of a student: name, age, grade
# Parameters needed to create an instance of a class: name, students

# Generate 10 random students
students = []
for i in range(10):
    name = f"Student{i+1}"
    age = random.randint(18, 25)
    grade = random.randint(1, 12)
    student = Student(name, age, grade)
    students.append(student)

# Generate 2 random classes
class1 = Class("Class1", [])
class2 = Class("Class2", [])

# Randomly assign students to classes
for student in students:
    if random.choice([True, False]):
        class1.students.append(student)
    else:
        class2.students.append(student)

# Print classes and students within the classes
print(f"Class {class1.name}:")
for student in class1.students:
    print(f"  {student.name}, Age: {student.age}, Grade: {student.grade}")

print(f"Class {class2.name}:")
for student in class2.students:
    print(f"  {student.name}, Age: {student.age}, Grade: {student.grade}")

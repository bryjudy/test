import random
from student_class import Student
from class_class import Class

students = []
classes = []

# Generate 10 random students
for i in range(10):
    student = Student(f"Student {i+1}")
    students.append(student)

# Generate 2 random classes
for i in range(2):
    class_name = f"Class {i+1}"
    class_students = random.sample(students, 5)
    new_class = Class(class_name, class_students)
    classes.append(new_class)

# Assign students to classes
for student in students:
    random_class = random.choice(classes)
    random_class.add_student(student)

# Print classes and students within the classes
for class_obj in classes:
    print(f"Class: {class_obj.name}")
    for student in class_obj.students:
        print(f"- {student.name}")

import random

student_class = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
class_class = ['Math', 'Science', 'History', 'English']

classroom = {class_name: [] for class_name in class_class}

for student in random.sample(student_class, 10):
    class_name = random.choice(class_class)
    classroom[class_name].append(student)

for class_name, students in classroom.items():
    print(f'{class_name}: {", ".join(students)}')

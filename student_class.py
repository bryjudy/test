class Student:
    def __init__(self, age, birthday='Unknown'):
        self.age = age
        self.birthday = birthday

    def get_age(self):
        return self.age

    def get_birthday(self):
        return self.birthday

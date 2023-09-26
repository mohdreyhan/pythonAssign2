class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender

    def say_hello(self):
        return f"hello {self.name}"

    def is_adult(self):
        if self.__age >= '18':
            return True
        else:
            return False

    def get__age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        Person.__init__(self, name, age, gender)
        self.student_id = student_id
        self.course = course

    def display_student_info(self):
        return f"{self.name} with student id {self.student_id} is studying in " \
               f"{self.course}"


class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, subject):
        Person.__init__(self, name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject

    def say_hello(self):
        return f"hello, my name is {self.name} and i am teaching {self.subject} subject"


Arun = Person("Arun", "25", "Male")
print(Arun.say_hello())
print(Arun.get__age())

Arun = Student("reyhan", "32", "Male", "101", "fsdm")
print(Arun.display_student_info())

Arun = Teacher("rakesh", "32", "Male", "111", "Python")
print(Arun.say_hello())

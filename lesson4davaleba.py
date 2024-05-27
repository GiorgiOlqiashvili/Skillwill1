class Student:
    # კლასის ატრიბუტი კლასისთვის
    university = "Default University"

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    # მეჯიქ მეთოდი
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    # მეთოდი "გადალახვისთვის"
    @property
    def is_passing(self):
        return self.grade > 60

    # მეთოდი ქულის გაზრდითვის
    def increase_grade(self, amount):
        self.grade += amount


# გამოყენება
student = Student("John Doe", 65, 20)
print(student)
print(student.is_passing)
student.increase_grade(10)
print(student)
print(student.is_passing)

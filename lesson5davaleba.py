class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class MixinAttributes:
    def display_attributes(self):
        attributes = [f"{attr}: {value}" for attr, value in self.__dict__.items()]
        return ", ".join(attributes)


class Student(Person, MixinAttributes):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university


student = Student("გიორგი", "ოლქიაშვილი", 20, "Skillwill")
print(student.display_attributes())

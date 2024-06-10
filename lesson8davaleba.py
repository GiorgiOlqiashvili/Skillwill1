class Person:
    def display_details(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Student(Person):
    def __init__(self, student_id, name):
        self._student_id = student_id
        self.name = name
        self._grades = {}

    @property
    def student_id(self):
        return self._student_id

    @property
    def grades(self):
        return self._grades

    def add_grade(self, subject, grade):
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            raise ValueError("Grade must be a number between 0 and 100")
        self._grades[subject] = grade

    def average_grade(self):
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)

    def display_details(self):
        return f"ID: {self.student_id}, Name: {self.name}, Average Grade: {self.average_grade():.2f}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student instances can be added")
        self.students.append(student)

    def show_student_details(self, student_id):
        student = self._find_student_by_id(student_id)
        if student:
            print(student.display_details())
        else:
            print(f"Student with ID {student_id} not found.")

    def show_student_average_grade(self, student_id):
        student = self._find_student_by_id(student_id)
        if student:
            print(f"Average Grade for {student.name} is {student.average_grade():.2f}")
        else:
            print(f"Student with ID {student_id} not found.")

    def _find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


if __name__ == "__main__":
    # ახალი სტუდენტის შექმნა
    student1 = Student(1, "Alice")
    student1.add_grade("Math", 95)
    student1.add_grade("Science", 85)

    student2 = Student(2, "Bob")
    student2.add_grade("Math", 80)
    student2.add_grade("Science", 90)

    # Student management system
    studentmanagement = StudentManagementSystem()
    studentmanagement.add_student(student1)
    studentmanagement.add_student(student2)

    # Display students details
    studentmanagement.show_student_details(1)
    studentmanagement.show_student_details(2)

    # საშუალო ქულა
    studentmanagement.show_student_average_grade(1)
    studentmanagement.show_student_average_grade(2)

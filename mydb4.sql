CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE Professors (
    professor_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthdate DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    department_id INT,
    professor_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    FOREIGN KEY (professor_id) REFERENCES Professors(professor_id)
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

SELECT Students.first_name, Students.last_name, Courses.course_name
FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.student_id
JOIN Courses ON Enrollments.course_id = Courses.course_id;

SELECT Courses.course_name, Professors.first_name, Professors.last_name
FROM Courses
LEFT JOIN Professors ON Courses.professor_id = Professors.professor_id;

SELECT Students.first_name, Students.last_name, Departments.department_name
FROM Students
RIGHT JOIN Departments ON Students.department_id = Departments.department_id;

SELECT Courses.course_name, Departments.department_name
FROM Courses
FULL OUTER JOIN Departments ON Courses.department_id = Departments.department_id;

SELECT Students.first_name, Students.last_name, Courses.course_name
FROM Students
CROSS JOIN Courses;

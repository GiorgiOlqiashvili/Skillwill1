CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    ClassID INT,
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);
CREATE TABLE Classes (
    ClassID INT PRIMARY KEY,
    ClassName VARCHAR(50)
);
CREATE TABLE StudentCourses (
    StudentID INT,
    CourseID INT,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
CREATE TABLE TeacherCourses (
    TeacherID INT,
    CourseID INT,
    PRIMARY KEY (TeacherID, CourseID),
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (1, 'Mathematics');
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (2, 'Science');

INSERT INTO Teachers (TeacherID, FirstName, LastName, DepartmentID) VALUES (1, 'John', 'Doe', 1);
INSERT INTO Teachers (TeacherID, FirstName, LastName, DepartmentID) VALUES (2, 'Jane', 'Smith', 2);

INSERT INTO Courses (CourseID, CourseName, DepartmentID) VALUES (1, 'Algebra', 1);
INSERT INTO Courses (CourseID, CourseName, DepartmentID) VALUES (2, 'Physics', 2);

INSERT INTO Classes (ClassID, ClassName) VALUES (1, '10A');
INSERT INTO Classes (ClassID, ClassName) VALUES (2, '10B');

INSERT INTO Students (StudentID, FirstName, LastName, ClassID) VALUES (1, 'Alice', 'Brown', 1);
INSERT INTO Students (StudentID, FirstName, LastName, ClassID) VALUES (2, 'Bob', 'Johnson', 2);

INSERT INTO StudentCourses (StudentID, CourseID) VALUES (1, 1);
INSERT INTO StudentCourses (StudentID, CourseID) VALUES (2, 2);

INSERT INTO TeacherCourses (TeacherID, CourseID) VALUES (1, 1);
INSERT INTO TeacherCourses (TeacherID, CourseID) VALUES (2, 2);

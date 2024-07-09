-- Create the table
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    salary FLOAT NOT NULL
);

-- Insert records
INSERT INTO employees (id, name, position, salary) VALUES (1, 'John Doe', 'Software Engineer', 75000);
INSERT INTO employees (id, name, position, salary) VALUES (2, 'Alice Smith', 'Data Analyst', 60000);
INSERT INTO employees (id, name, position, salary) VALUES (3, 'Bob Johnson', 'Project Manager', 85000);

-- Select all records
SELECT * FROM employees;

-- Select specific columns
SELECT name, position FROM employees;

-- Select with a condition
SELECT * FROM employees WHERE salary > 65000;

-- Update a record
UPDATE employees SET salary = 80000 WHERE id = 1;

-- Update multiple columns
UPDATE employees SET position = 'Senior Software Engineer', salary = 90000 WHERE id = 1;

-- Delete a record
DELETE FROM employees WHERE id = 1;

-- Delete all records
DELETE FROM employees;



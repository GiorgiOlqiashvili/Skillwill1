CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10, 2),
    quantity INT,
    color VARCHAR(20),
    length DECIMAL(10, 2),
    width DECIMAL(10, 2)
);

INSERT INTO products (id, name, price, quantity, color, length, width) VALUES
(1, 'Iphone XR', 650.00, 3, 'Blue', 5.0, 2.5),
(2, 'Samsung galaxy s10', 550.00, 5, 'Red', 4.0, 2.0),
(3, 'Google pixel 6', 700.00, 1, 'Blue', 5.5, 2.7),
(4, 'Xiaomi Redmi Note 10', 800.00, 4, 'Green', 4.5, 2.1),
(5, 'Iphone XS', 600.00, 6, 'Blue', 5.2, 2.1);

SELECT * FROM products WHERE price > 600;

SELECT * FROM products WHERE quantity > 2 AND color = 'Blue';

SELECT id, name, quantity, price, quantity * price AS total_value FROM products;

SELECT id, name, price, quantity, color, length, width, (length * width) AS area
FROM products
WHERE (length * width) > 10;



CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);


INSERT INTO Products (name, category, price) VALUES 
('Laptop', 'Electronics', 1000),
('Smartphone', 'Electronics', 300),
('PC', 'Electronics', 205),
('Oven', 'Home Appliances', 710),
('Tablet', 'Electronics', 450),
('Blender', 'Home Appliances', 500),
('TV', 'Electronics', 1500);


EXPLAIN ANALYZE SELECT * FROM Products WHERE category = 'Electronics';

CREATE INDEX idx_category ON Products(category);

EXPLAIN ANALYZE SELECT * FROM Products WHERE category = 'Electronics';

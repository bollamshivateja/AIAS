CREATE DATABASE IF NOT EXISTS sample_db;

USE sample_db;

CREATE TABLE IF NOT EXISTS sample_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    value DECIMAL(10,2),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO sample_table (name, value) VALUES
    ('Alice', 123.45),
    ('Bob', 67.89),
    ('Charlie', 250.00),
    ('Diana', 99.99);

SELECT * FROM sample_table;

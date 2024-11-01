CREATE DATABASE todo_list_db;
USE todo_list_db;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending'
);

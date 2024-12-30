CREATE DATABASE users_schema;

USE users_schema;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    email varchar(45),
    created_at DATETIME,
    updated_at DATETIME
);


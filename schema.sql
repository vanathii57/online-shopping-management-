-- 1. Create the database
CREATE DATABASE IF NOT EXISTS online_shop_db;

-- 2. Use the database
USE online_shop_db;

-- 3. Create 'users' table to store form data from index.html
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- 4. Create 'contacts' table to store messages from contact.html
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL
);

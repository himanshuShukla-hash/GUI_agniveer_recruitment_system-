-- Create AgniVeer Database
CREATE DATABASE IF NOT EXISTS AgniVeer;

-- Use the database
USE AgniVeer;

-- Create recruitdata table to store recruit information
CREATE TABLE IF NOT EXISTS recruitdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    qualification VARCHAR(100),
    height DECIMAL(5,2),
    address VARCHAR(255),
    weight DECIMAL(5,2),
    percentage DECIMAL(5,2)
);

-- Create recruitlogincred table for recruit login credentials
CREATE TABLE IF NOT EXISTS recruitlogincred (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mail VARCHAR(100),
    pwd VARCHAR(100)
);

-- Create officerlogincred table for officer login credentials
CREATE TABLE IF NOT EXISTS officerlogincred (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mail VARCHAR(100),
    pwd VARCHAR(100)
);

-- Insert sample data (optional)
INSERT INTO recruitdata (name, age, qualification, height, address, weight, percentage) 
VALUES 
('Aditya Kalitha', 18, '10+2', 170.0, 'SHIMLA', 45, 80),
('Pranjal Singh', 19, '10+2', 170.0, 'GHI', 60, 99),
('Agrim', 20, '10+2', 170.0, 'ABC', 50, 100),
('Barthian Prithuvasai', 18, '10+2', 180.0, 'BHU', 60, 100),
('Akshar Ashikari', 18, '10+2', 170.0, 'DBY', 70, 85),
('Himanshu Shukla', 18, '10+2', 170.0, 'BYD', 60, 95);

INSERT INTO recruitlogincred (name, mail, pwd)
VALUES 
('Himanshu Shukla', 'himanshu@gmail.com', 'pass123');

INSERT INTO officerlogincred (name, mail, pwd)
VALUES 
('Vedansh Gandharva', 'vedansh@agni.com', 'officer123');

-- Display table structures
DESC recruitdata;
DESC recruitlogincred;
DESC officerlogincred;

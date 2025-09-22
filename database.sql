-- database.sql
-- Create the database
CREATE DATABASE IF NOT EXISTS blood_bank;
USE blood_bank;

-- Create the blood_stock table
CREATE TABLE IF NOT EXISTS blood_stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    blood_type VARCHAR(5) NOT NULL,
    quantity INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    collection_date DATE NOT NULL
);

-- Insert some sample data
INSERT INTO blood_stock (blood_type, quantity, location, collection_date) VALUES
('A+', 50, 'Bengaluru Main Center', '2023-11-01'),
('B+', 45, 'Bengaluru West Center', '2023-10-25'),
('O-', 25, 'Bengaluru Main Center', '2023-11-03'),
('AB+', 15, 'Bengaluru South Center', '2023-11-02');

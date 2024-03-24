-- Create database if not exists
-- Create user if not exists and set password
-- Grant privileges to the user hbnb_test on the database hbnb_test_db
-- Grant SELECT privilege to the user hbnb_test on the performance_schema database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';

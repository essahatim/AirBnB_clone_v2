-- Create database if not exists
-- Create user if not exists and set password
-- Grant privileges to the user hbnb_dev on the database hbnb_dev_db
-- Grant SELECT privilege to the user hbnb_dev on the performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';

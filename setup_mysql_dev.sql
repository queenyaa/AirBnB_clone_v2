-- Switch to mysql database
USE mysql;

-- Create the database if it doesn't exit
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the uder if it doesn't exit
CREATE USER IF NOT EXISTS 'hbtn_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- FLUSH PRIVILEGES;

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

EXIT;

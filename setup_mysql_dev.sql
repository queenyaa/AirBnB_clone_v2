-- Switch to mysql database
-- USE mysql;
GRANT CREATE USER ON *.* TO 'root'@'localhost';
GRANT GRANT OPTION ON *.* TO 'root'@'localhost';

-- Create the database if it doesn't exit
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the uder if it doesn't exit
CREATE USER IF NOT EXISTS 'hbtn_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL
ON `hbnb_dev_db`.*
TO 'hbnb_dev'@'localhost';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;

-- EXIT;

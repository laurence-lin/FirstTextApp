CREATE DATABASE IF NOT EXISTS firsttext;
USE firsttext;

CREATE TABLE IF NOT EXISTS textapp_textinference (
    id INT AUTO_INCREMENT PRIMARY KEY,
    originText TEXT(65535),
    inferenceText TEXT(65535),
    task_type VARCHAR(50),
    user_ip VARCHAR(30),
    update_time DATETIME
);


CREATE USER IF NOT EXISTS 'admin'@'%' IDENTIFIED BY 'laurence';
GRANT ALL PRIVILEGES ON firsttext.* TO 'admin'@'%';
FLUSH PRIVILEGES;
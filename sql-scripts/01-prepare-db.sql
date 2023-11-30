DROP DATABASE IF EXISTS todos;
DROP USER  IF EXISTS 'todo_user'@'localhost';
CREATE DATABASE todos;
CREATE USER 'todo_user'@'localhost' IDENTIFIED BY 'todo_password';
GRANT ALL PRIVILEGES ON todos.* TO 'todo_user'@'localhost';
FLUSH PRIVILEGES;

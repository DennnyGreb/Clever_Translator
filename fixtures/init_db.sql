-- To use it:
-- 1. login into MySQL as root
--      mysql -u root -p
-- 2. run this script
--      source <path to the file>/init_db.sql
-- 3. grant all rights on this DB for your work user
--      CREATE USER '<user_name>'@'localhost' IDENTIFIED BY '<password>';
--      GRANT ALL ON TRANSLATING.* TO '<user_name>'@'localhost';

-- create db. CHARACTER SET!!!
DROP DATABASE IF EXISTS TRANSLATING;
CREATE DATABASE IF NOT EXISTS TRANSLATING CHARACTER SET utf8;

-- switch to ur db
USE TRANSLATING;

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Roles;
DROP TABLE IF EXISTS Word;

-- table User
CREATE TABLE IF NOT EXISTS `User` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255),
  `surname` VARCHAR(255),
  `email` VARCHAR(255),
  `password` VARCHAR(255),
  `role_id` INTEGER,
  PRIMARY KEY (`id`)
);

-- table Roles
CREATE TABLE IF NOT EXISTS `Roles` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255),
  PRIMARY KEY (`id`)
);

-- table Word
CREATE TABLE IF NOT EXISTS `Word` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `user_id` INTEGER,
  `word_text` VARCHAR(255),
  PRIMARY KEY (`id`)
);

-- Add foreign key for User to provide roles
ALTER TABLE `User` ADD CONSTRAINT `fk-user-role` FOREIGN KEY (role_id) REFERENCES `Roles` (id);
-- Add foreign key for Word to save user's words'
ALTER TABLE `Word` ADD CONSTRAINT `fk-word-user` FOREIGN KEY (user_id) REFERENCES `User` (id);

INSERT INTO Roles (name) VALUES ("User");
INSERT INTO Roles (name) VALUES ("Admin");

INSERT INTO User (name, surname, email, password, role_id) 
VALUES ("Denis", "Grebenets", "dendendengrebenets@gmail.com", "qwerty", 1);

INSERT INTO Word (user_id, word_text) VALUES (1, "God");

SHOW TABLES;

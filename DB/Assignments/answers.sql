-- Write an SQL query to create a new database called salesDB.
CREATE DATABASE salesDB;
USE salesDB;
-- salesDB contains information about customers,products and sales personnel
-- creating the customer table
CREATE TABLE customer_data (
	customer_id VARCHAR(50) PRIMARY KEY NOT NULL,
    customer_name VARCHAR(100)
);

-- creating the product table
CREATE TABLE product_data (
	product_id VARCHAR(50) PRIMARY KEY NOT NULL,
    product_name VARCHAR(100),
    product_price INT
);

-- creating the sales personnel table
CREATE TABLE sales_person_data (
	sales_person_id VARCHAR(50) PRIMARY KEY NOT NULL,
    customer_id VARCHAR(50),
    product_id VARCHAR(50)
);

-- Write an SQL query to drop (delete) the database called demo.
CREATE DATABASE demo;
DROP DATABASE demo;
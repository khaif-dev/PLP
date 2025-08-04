CREATE DATABASE salesDB;
USE salesDB;
CREATE TABLE customer_data (
	customer_id VARCHAR(50) PRIMARY KEY NOT NULL,
    customer_name VARCHAR(100)
);

CREATE TABLE product_data (
	product_id VARCHAR(50) PRIMARY KEY NOT NULL,
    product_name VARCHAR(100),
    product_price INT
);

CREATE TABLE sales_person_data (
	sales_person_id VARCHAR(50) PRIMARY KEY NOT NULL,
    customer_id VARCHAR(50),
    product_id VARCHAR(50)
);

CREATE DATABASE schoolDB;
DROP DATABASE schoolDB;
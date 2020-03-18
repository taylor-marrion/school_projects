/*
    Title: project3_create.sql
    Author: Taylor Marrion
    Date: 2/23/2020
    Notes: 
*/

-- DROP all tables if they already exist before creating
DROP TABLE IF EXISTS rental;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS product_order;
DROP TABLE IF EXISTS distributor;
DROP TABLE IF EXISTS movie_title;
DROP TABLE IF EXISTS actor;
DROP TABLE IF EXISTS director;
DROP TABLE IF EXISTS academy_award;

-- CREATE tables
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    phone VARCHAR(12), -- includes space for '-' characters
    street VARCHAR(30),
    city VARCHAR(30),
    state VARCHAR(2), -- 2 letter state abbreviation
    zip VARCHAR(5)
);

CREATE TABLE product (
    title_id VARCHAR(20),
    product_type VARCHAR(3), -- (VHS/DVD)
    PRIMARY KEY(title_id, product_type),
    is_rewound VARCHAR(1),  -- (T/F)
    dist_id VARCHAR(10),
    dist_serial VARCHAR(10),
    price DECIMAL(4,2)
);

CREATE TABLE rental (
    customer_id INT,
    out_date DATETIME,
    PRIMARY KEY(customer_id, out_date),
    title_id VARCHAR(20),
    product_type VARCHAR(3), -- (VHS/DVD)
    return_date DATETIME,
    is_late VARCHAR(1), -- (T/F)
    is_damaged VARCHAR(1), -- (T/F)
    fees_due DECIMAL(5,2),
    discount DECIMAL(2,2),
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
    FOREIGN KEY(title_id, product_type) REFERENCES product(title_id, product_type) ON DELETE SET NULL
);

CREATE TABLE product_order(
    invoice VARCHAR(10) PRIMARY KEY,
    dist_id VARCHAR(10),
    order_date DATETIME,
    receive_date DATETIME,
    is_received VARCHAR(1), -- (T/F)
    quantity INT,
    cost DECIMAL(7,2)
);

CREATE TABLE distributor(
    dist_id VARCHAR(10) PRIMARY KEY,
    dist_name VARCHAR(50),
    phone VARCHAR(12), -- includes space for '-' characters
    street VARCHAR(30),
    city VARCHAR(30),
    state VARCHAR(2), -- 2 letter state abbreviation
    zip VARCHAR(5)
);

ALTER TABLE product_order
ADD FOREIGN KEY(dist_id)
REFERENCES distributor(dist_id)
ON DELETE SET NULL;

ALTER TABLE product
ADD FOREIGN KEY(dist_id)
REFERENCES product_order(dist_id)
ON DELETE SET NULL;

CREATE TABLE movie_title(
    title_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(30),
    category VARCHAR(20),
    rating VARCHAR(5), -- G, PG, PG-13, R
    year_made YEAR,
    run_length TIME,
    director VARCHAR(10),
    starring VARCHAR(10),
    award_category VARCHAR(20),
    award_year YEAR
);

ALTER TABLE product
ADD FOREIGN KEY(title_id)
REFERENCES movie_title(title_id)
ON DELETE CASCADE;

CREATE TABLE actor(
    actor_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);

ALTER TABLE movie_title
ADD FOREIGN KEY(starring)
REFERENCES actor(actor_id)
ON DELETE SET NULL;

CREATE TABLE director(
    director_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);

ALTER TABLE movie_title
ADD FOREIGN KEY(director)
REFERENCES director(director_id)
ON DELETE SET NULL;

CREATE TABLE academy_award(
    award_category VARCHAR(20),
    award_year YEAR,
    PRIMARY KEY(award_category, award_year),
    winner VARCHAR(40)
);

ALTER TABLE movie_title
ADD FOREIGN KEY(award_category, award_year)
REFERENCES academy_award(award_category, award_year)
ON DELETE SET NULL;

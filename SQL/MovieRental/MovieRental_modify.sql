/*
    Title: project3_modify.sql
    Author: Taylor Marrion
    Date: 2/23/2020
    Notes: 
*/

-- Retrieve all of your customers info, sorted by account number.
SELECT * FROM customer;

-- Retrieve all videos rented in last 30 days, sort in chronological rental date order.
SELECT * FROM rental
WHERE out_date
BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW();

-- List your distributors and all their information sorted in order by company name.
SELECT * from distributor
ORDER BY dist_name;

-- Update a customer's maiden name, using PRIMARY KEY in WHERE clause.
UPDATE customer
SET last_name = 'Majors'
WHERE customer_id = 1249;

-- Delete a customer from the database, usinhg PRIMARY KEY in WHERE clause.
DELETE FROM customer
WHERE customer_id = 1262;

-- Repeat command to display changes made to customer table
SELECT * FROM customer;
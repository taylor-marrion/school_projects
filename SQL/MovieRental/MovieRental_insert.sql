/*
    Title: project3_insert.sql
    Author: Taylor Marrion
    Date: 2/23/2020
    Notes: Order is set to minimize updating FOREIGN KEY after initial entry
*/

INSERT INTO customer VALUES
(1,'Patrick','Bateman','212-555-6342','358 Exchange Place','New York','NY','10099');
INSERT INTO customer VALUES
(2,'Peter','Gibbons','310-333-9820','4120 Freidrich Lane','Austin','TX','78744');
INSERT INTO customer VALUES
(3,'Janet','Weiss','104-304-6652','1 Oakley Court','Mansion','PA','15105');
INSERT INTO customer VALUES
(4,'Brad','Majors','236-345-2099','1 Oakley Court','Mansion','PA','15105');
INSERT INTO customer VALUES
(5,'David','Lightman','778-825-9328','333 Arden Blvd','Los Angeles','CA','90020');
INSERT INTO customer VALUES
(6,'Dade','Murphy','581-204-4385','31 Grove St','New York','NY','10014');

INSERT INTO academy_award VALUES
('Director',2018,'Guillermo Del Toro');
INSERT INTO academy_award VALUES
('Director',2015,'Alejandro Inarritu');
INSERT INTO academy_award VALUES
('Supporting Actor',2009,'Heath Ledger');
INSERT INTO academy_award VALUES
('Film of the Year',2005,'Brad Bird');
INSERT INTO academy_award VALUES
('Sound Editing',2017,'Sylvain Bellemare');
INSERT INTO academy_award VALUES
('Writing',2014,'Spike Jonze');

INSERT INTO actor VALUES
('AA001234','Elisa','Esposito');
INSERT INTO actor VALUES
('AA009428','Michael','Keaton');
INSERT INTO actor VALUES
('AA001672','Christian','Bale');
INSERT INTO actor VALUES
('AA003902','Craig','Nelson');
INSERT INTO actor VALUES
('AA003356','Amy','Adams');
INSERT INTO actor VALUES
('AA007821','Joaquin','Phoenix');

INSERT INTO director VALUES
('DD003921','Guillermo','Del Toro');
INSERT INTO director VALUES
('DD003891','Alejandro','Inarritu');
INSERT INTO director VALUES
('DD001267','Christopher','Nolan');
INSERT INTO director VALUES
('DD002836','Brad','Bird');
INSERT INTO director VALUES
('DD002803','Denis','Villeneuve');
INSERT INTO director VALUES
('DD006652','Spike','Jonze');

INSERT INTO movie_title VALUES
('DT001245','The Shape of Water','Drama/Thriller','R',2017,02:03:00,'DD003921','AA001234','Director',2018);
INSERT INTO movie_title VALUES
('D0001789','Birdman','Drama','R',2014,01:59:00,'DD003891','AA009428','Director',2015);
INSERT INTO movie_title VALUES
('DT008392','Batman: The Dark Knight','Drama/Thriller','PG-13',02:32:00,2008,'DD001267','AA001672','Supporting Actor',2009);
INSERT INTO movie_title VALUES
('AA007320','The Incredibles','Action/Adventure','PG',01:55:00,2004,'DD002836','AA003902','Film of the Year',2005);
INSERT INTO movie_title VALUES
('DM006732','Arrival','Drama/Mystery','PG-13',01:56:00,2016,'DD002803','AA003356','Sound Editing',2017);
INSERT INTO movie_title VALUES
('DR003381','Her','Drama/Romance','R',02:06:00,2013,'DD006652','AA007821','Writing',2014);

INSERT INTO distributor VALUES
('DI001234','Big Ed Video Supply','878-555-2345','12 Some st.','Somecity','VA','23220');
INSERT INTO distributor VALUES
('DI001346','Mid-Atlantic Movies','804-555-5641','89 Other st.','Othercity','MD','32189');
INSERT INTO distributor VALUES
('DI002389','Eastern Hollywood','723-555-9032','135 Main st.','Newcity','VA','23219');
INSERT INTO distributor VALUES
('DI002589','Another Distributor','432-555-1278','1832 1st Ave.','Somecity','VA','23220');
INSERT INTO distributor VALUES
('DI003490','More Movie Distribution','324-555-6782','1451 3rd st.','Othercity','MD','32188');
INSERT INTO distributor VALUES
('DI003336','Stillmore Movies','459-555-1093','672 Different st.','Diffcity','WV','34091');

INSERT INTO product_order VALUES
('','DI001234',,,'',,);
INSERT INTO product_order VALUES
('','DI001346',,,'',,);
INSERT INTO product_order VALUES
('','DI002389',,,'',,);
INSERT INTO product_order VALUES
('','DI002589',,,'',,);
INSERT INTO product_order VALUES
('','DI003490',,,'',,);
INSERT INTO product_order VALUES
('','',,,'',,);

INSERT INTO product VALUES
('','DVD','T', NULL ,'458292','14.99');
INSERT INTO product VALUES
('','DVD','T', NULL ,'189245','14.99');
INSERT INTO product VALUES
('','VHS','T', NULL ,'274528','10.99');
INSERT INTO product VALUES
('','DVD','T', NULL ,'290476','14.99');
INSERT INTO product VALUES
('','VHS','T', NULL ,'002371','10.99');
INSERT INTO product VALUES
('','DVD','T', NULL ,'902178','14.99');

INSERT INTO rental VALUES
(,,'','',,'F','F',000.00,.00,);
INSERT INTO rental VALUES
(,,'','',,'F','F',000.00,.00,);
INSERT INTO rental VALUES
(,,'','',,'F','F',000.00,.00,);
INSERT INTO rental VALUES
(,,'','',,'F','F',000.00,.00,);
INSERT INTO rental VALUES
(,,'','',,'F','F',000.00,.00,);
INSERT INTO rental VALUES
(,,'','',,'F','F',000.00,.00,);


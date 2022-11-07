CREATE TABLE Customer(
Customer_number INT,
First_name VARCHAR(30),
Last_name VARCHAR(30),
Customer_balance decimal(6,2),
PRIMARY KEY(Customer_number)
);

CREATE TABLE INVOICE(
invoice_number INT,
INVOICE_DATE DATE,
INVOICE_amount decimal(6,2),
Customer_number INT,
PRIMARY KEY (invoice_number),
FOREIGN KEY (Customer_number) REFERENCES Customer(Customer_number)
);

Insert into Customer values (1000,'smith','jaanne',1050.11);

Insert into invoice values (8000,'2016-03-23',235.89,1000);
Insert into invoice values (8001,'2016-03-23',312.82,1001);
Insert into invoice values (8002,'2016-03-30',528.10,1001);
Insert into invoice values (8003,'2016-04-12',194.78,1000);
Insert into invoice values (8004,'2016-04-23',619.44,1000);


alter table customer auto_increment = 5000;

ALTER TABLE customer ADD CUST_DOB DATE;


UPDATE Customer SET CUST_DOB = '2016-03-23' WHERE First_name='smith';



SET SQL_SAFE_UPDATES=0;
UPDATE Customer SET CUST_DOB = '2016-03-23' WHERE First_name='smith';
SET SQL_SAFE_UPDATES=1;

Insert into Customer values (5,'yourname','surname',500);


--CREATE TABLE CustomerOrder (cust_id NUMBER, order_date DATE,cust_name VARCHAR2(100),
--last_name VARCHAR2(50),EMAIL_COM VARCHAR2(250), cont_no VARCHAR2(100));  
--insert into CustomerOrder 
--VALUES ( 102,TO_DATE('06 20,2025', 'MM DD,YYYY'),'amit', 'shah', 'amitthecm@GMAIL.COM', NULL);
--
UPDATE CustomerOrder SET EMAIL_COM= 'amgmail.com' WHERE cust_id =102;
select * from CustomerOrder; 
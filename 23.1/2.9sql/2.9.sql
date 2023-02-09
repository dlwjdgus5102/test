-- 문제 1
select * from employees;

-- 문제 2
select customernumber,customername from customers;

-- 문제 3
select firstname,lastname,email from employees order by firstname;

-- 문제 4
select firstname as '이름',lastname as '성',email as '이메일' from employees order by firstname;

-- 문제 5
select employeenumber,lastname,firstname,officecode,jobtitle from employees order by jobtitle desc, officecode desc;

-- 문제 6
select * from orderdetails order by quantityOrdered, priceEach;

-- 문제 7
select customerNumber, country, contactFirstName from customers order by contactFirstName desc, country;

-- 문제 8
select productCode, quantityInStock, buyPrice,quantityInStock * buyPrice from products ORDER BY quantityInStock * buyPrice desc;
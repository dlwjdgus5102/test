-- 문제 1
select DISTINCT country from customers order by country;

-- 문제 2
select distinct state from customers order by state desc;

-- 문제 3
select customernumber, customername, country from customers where country != 'usa' order by customerNumber desc;

-- 문제 4
select * from offices where city = 'paris';

-- 문제 5
select customernumber, customername, country, state from customers where country = 'usa' and state = 'ca' order by customerName desc;

-- 문제 6
select customernumber, customername, country, state from customers where country = 'usa' and state = 'ca' or state = 'ny' order by  customernumber desc;

-- 문제 7
select customernumber, customername, state from customers where state in ('ca','ny','ct','pa') order by customerNumber desc;

-- 문제 8
select productcode, productname, quantityInStock from products where quantityInStock < 1000 order by quantityInStock;

-- 문제 9
select productcode, productname, quantityInStock from products where quantityInStock between 2000 and 3000 order by quantityInStock desc;

-- 문제 10
select customernumber, customername, phone from customers where phone like '%555' order by customerName desc;

-- 문제 11
select productcode, quantityInStock from products order by quantityInStock desc limit 5;

-- 문제 12
select jobtitle from employees group by jobTitle order by jobTitle desc;

-- 문제 13
select country from customers group by country order by country desc;

-- 문제 14
select ordernumber, sum(quantityOrdered * priceEach) from orderdetails group by orderNumber order by sum(quantityOrdered * priceEach) desc;

-- 문제 15


-- 문제 16
select productline,max(quantityInStock) from products group by productLine having max(quantityInStock) < 9000;

-- 문제 17
select ordernumber,sum(quantityordered),sum(priceeach * quantityOrdered) from orderdetails group by ordernumber having sum(quantityordered) > 500 and sum(priceeach * quantityOrdered) > 50000;
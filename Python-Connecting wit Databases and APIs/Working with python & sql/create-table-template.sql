-- Active: 1690611250646@@127.0.0.1@3306@test
CREATE TABLE if NOT exists  test1.test_table (c1 INT, c2 VARCHAR(50), c3 FLOAT, c4 INT, c5 VARCHAR(50));

CREATE TABLE if NOT exists  test2.test_table (c1 INT, c2 VARCHAR(50), c3 FLOAT, c4 INT, c5 VARCHAR(50));

insert into test1.test_table values(123, 'Emdadul', 32.3,  456, 'Tareque');

SELECT * FROM test1.test_table
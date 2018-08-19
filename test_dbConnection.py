#!/usr/bin/python
#install-- sudo apt-get install python-mysqldb
import sys
import pytest
import MySQLdb

def test_dbconnection():
	import MySQLdb

	# Open database connection
	db = MySQLdb.connect("localhost","root","root","raghu_test_db" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Drop table if it already exist using execute() method.
	cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

	# Create table as per requirement
	sql = """CREATE TABLE EMPLOYEE (
        	 FIRST_NAME  CHAR(20) NOT NULL,
         	 LAST_NAME  CHAR(20),
         	 AGE INT,  
         	 SEX CHAR(1),
         	 INCOME FLOAT )"""
	sql1 = """insert into EMPLOYEE values('Raghu','Bhat',37,'M',25000);"""
	sql2 = """SELECT AGE FROM EMPLOYEE """
	#print("AGE=",sql1)
	#sql1 = """DESC EMPLOYEE"""

	cursor.execute(sql)
	cursor.execute(sql1)
	
	cursor.execute("insert into EMPLOYEE values('Ayush','B',07,'M',2000)")
	cursor.execute(sql2)
	out = cursor.fetchone()
	for i in out:
		print(i)
	assert i == 37 
	# disconnect from server
	db.close()

#test_dbconnection()

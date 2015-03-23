#!/usr/bin/python

# NFC Attendance System
# Date Last Modified : 24-03-2015
# Authors : Anagh Kumar Baranwal, Manush Bhatt, Arnav Nag
# License : GPLv3

import MySQLdb

def init():
	db = MySQLdb.connect(host="localhost",user="admin",passwd="admin123",db="nasadb")
	cur=db.cursor()

	sql = """CREATE TABLE STUDENT (
	 	C_ID INT NOT NULL,
	 	R_ID INT(10) NOT NULL,
         	FIRST_NAME  CHAR(20) NOT NULL,
         	LAST_NAME  CHAR(20),
         	AGE INT,
		PRIMARY KEY (R_ID) )"""

	cur.execute(sql)
	db.close()
	
def add(values):
	db = MySQLdb.connect(host="localhost",user="admin",passwd="admin123",db="nasadb")
	cur=db.cursor()

	sql = """INSERT INTO STUDENT VALUES (VALUES)"""

	cur.execute(sql)
	db.close()

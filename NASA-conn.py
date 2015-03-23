#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",user="manush",passwd="manush123",db="nasadb")

cur=db.cursor()

sql = """CREATE TABLE STUDENT (
	 C_ID INT NOT NULL
	 R_ID INT(10) NOT NULL,
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT
	PRIMARY KEY (R_ID) )"""

cur.execute(sql)
db.close()

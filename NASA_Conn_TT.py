import MySQLdb
from invalid_led import invalid

def init():
	i=0
	for i in range(5):
		d=str(i+1)
		day="day"+d
		db = MySQLdb.connect(host="localhost",user="admin",passwd="admin123",db=day)
		cur=db.cursor()

		h1 = """CREATE TABLE h1 (
			C_ID BIGINT NOT NULL,
			R_ID INT(10) NOT NULL,
			FIRST_NAME  CHAR(20) NOT NULL,
			LAST_NAME  CHAR(20),
			PRIMARY KEY (R_ID) )"""

		cur.execute(h1)
		h2="""CREATE TABLE h2 LIKE h1;"""
		h3="""CREATE TABLE h3 LIKE h1;"""
		h4="""CREATE TABLE h4 LIKE h1;"""
		h5="""CREATE TABLE h5 LIKE h1;"""
		h6="""CREATE TABLE h6 LIKE h1;"""
		h7="""CREATE TABLE h7 LIKE h1;"""
		cur.execute(h2)
		cur.execute(h3)
		cur.execute(h4)
		cur.execute(h5)
		cur.execute(h6)
		cur.execute(h7)
		db.commit()
		db.close()
def add(c,r,f,l):
	i=0
	for i in range(5):
		d=str(i+1)
		day="day"+d
		db = MySQLdb.connect(host="localhost",user="admin",passwd="admin123",db=day)
		cur=db.cursor()
		h1 = ("INSERT INTO h1 VALUES ('%s','%s','%s','%s');"% (c,r,f,l))
		h2 = ("INSERT INTO h2 VALUES ('%s','%s','%s','%s');"% (c,r,f,l))
		h3 = ("INSERT INTO h3 VALUES ('%s','%s','%s','%s');"% (c,r,f,l))
		h4 = ("INSERT INTO h4 VALUES ('%s','%s','%s','%s');"% (c,r,f,l))
		h5 = ("INSERT INTO h5 VALUES ('%s','%s','%s','%s');"% (c,r,f,l))
		h6 = ("INSERT INTO h6 VALUES ('%s','%s','%s','%s');"% (c,r,f,l))
		h7 = ("INSERT INTO h7 VALUES ('%s','%s','%s','%s');"% (c,r,f,l))
		cur.execute(h1)
		cur.execute(h2)
		cur.execute(h3)
		cur.execute(h4)
		cur.execute(h5)
		cur.execute(h6)
		cur.execute(h7)
		db.commit()
		db.close()

def check(value):
	db = MySQLdb.connect(host="localhost",user="admin",passwd="admin123",db="nasadb")
	cur=db.cursor()
	cur.execute("Use day1;")
	sql =( " SELECT * FROM h1 WHERE C_ID = %s ;"% (value))
	cur.execute(sql)
	
	#  USE cursor.fetchone()[0] if using COUNT(*)
	row = cur.fetchone()
	
	if row is None:
		invalid()
		print "Invalid ID"
	else:
		print "WELCOME ",row[1]



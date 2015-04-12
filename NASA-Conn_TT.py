import MySQLdb

def init():
	i=0
	for i in range(5):
		d=str(i+1)
		day="day"+d
		db = MySQLdb.connect(host="localhost",user="admin",passwd="admin123",db=day)
		cur=db.cursor()

		h1 = """CREATE TABLE h1 (
			C_ID INT NOT NULL,
			R_ID INT(10) NOT NULL,
			NAME  CHAR(20) NOT NULL,
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
		db.close()
init()

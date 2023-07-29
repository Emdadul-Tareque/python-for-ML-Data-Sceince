import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if NOT exists  test3.test_table (c1 INT, c2 VARCHAR(50), c3 FLOAT, c4 INT, c5 VARCHAR(50));")

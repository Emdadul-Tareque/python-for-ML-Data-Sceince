import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("insert into test1.test_table values(123, 'Emdadul', 32.3,  456, 'Tareque');")
for i in range(10):
    mycursor.execute("insert into test1.test_table values(123, 'Emdadul', 32.3,  456, 'Tareque');")

mydb.commit()
mydb.close()

import mysql.connector
import MySQLdb
mydb=MySQLdb.connect(host='localhost',user='root',password='root',database='exampledb')
my_cursor=mydb.cursor()
# to create table
#my_cursor.execute('CREATE TABLE example(name varchar(50),age smallint UNSIGNED)')
# to insert the data
#sql_query='INSERT INTO example(name,age)values(%s,%s) '
#data=[('suresh',27),
 #     ('mahesh',28),
  #    ('ram',34)]
#to execute into tables
#my_cursor.executemany(sql_query,data)
my_cursor.execute('select * from example')
res=my_cursor.fetchall()
for i in res:
    print(i)

# to get one value form table
#my_cursor.execute('select * name example')
#res=my_cursor.fetchone()
#print(res)
# to update
#sql_qry='UPDATE example SET age=30 WHERE name="suresh"'
#sql_qry='UPDATE example SET name="virat" WHERE age=30'
#my_cursor.execute(sql_qry)
# to delete
sql='DELETE FROM example WHERE age="30"'
my_cursor.execute(sql)


    
mydb.commit()


    
                           
                           



    
    

import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(host="localhost", username="root", passwd="Shrutiagr31@", database="sales")

# cursor:
# they are bound to the connection for the entire lifetime and all the commands are executed in
# the context of the database session wrapped by the connection.
my_cursor = mydb.cursor()

# creating a table
# my_cursor.execute("create table test(id int primary key not null auto_increment, name varchar(50) not null, created datetime not null, gender enum('M', 'F', 'O') not null)")

# inserting into table
# my_cursor.execute("insert into test(name, created, gender) values(%s, %s, %s)", ("Shruti", datetime.now(), 'F'))
# my_cursor.execute("insert into test(name, created, gender) values(%s, %s, %s)", ("Komil", datetime.now(), 'M'))
# my_cursor.execute("insert into test(name, created, gender) values(%s, %s, %s)", ("Riya", datetime.now(), 'F'))
# my_cursor.execute("insert into test(name, created, gender) values(%s, %s, %s)", ("Kanishka", datetime.now(), 'F'))
# my_cursor.execute("insert into test(name, created, gender) values(%s, %s, %s)", ("Akshat", datetime.now(), 'M'))

# fetching values from table
print("FETCHING ALL ROWS: ")
my_cursor.execute("select * from test")
res = my_cursor.fetchall()
for i in res:
    print(i)

print("\nFETCHING ALL FEMALES: ")
my_cursor.execute("select id, first_name from test where gender = 'F' order by id, first_name asc")
females = my_cursor.fetchall()
for i in females:
    print(i)

# my_cursor.execute("alter table test add column food varchar(20) not null")
print("\nDESCRIBE TEST(after adding food column): ")
my_cursor.execute("describe test")
for i in my_cursor:
    print(i)


# my_cursor.execute("\nAlter table test drop food")
# print("DESCRIBE TEST (after dropping food column): ")
# my_cursor.execute("describe test")
# for i in my_cursor:
#     print(i)

# my_cursor.execute("alter table test change name first_name varchar(20)")
# my_cursor.execute("alter table test add column last_name varchar(20) not null")

# updating last names to every row
my_cursor.execute("update test set last_name = 'Agarwal' where first_name = 'shruti'")
my_cursor.execute("update test set last_name = 'Singhal' where first_name = 'komil'")
my_cursor.execute("update test set last_name = 'Kataria' where first_name = 'kanishka'")
my_cursor.execute("update test set last_name = 'Mehta' where first_name = 'riya'")
my_cursor.execute("update test set last_name = 'Shah' where first_name = 'akshat'")

print('\n id \tfName \tlName ')
my_cursor.execute('select id, first_name, last_name from test')
for i in my_cursor:
    print(i)
mydb.commit()



import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="root", passwd="Shrutiagr31@", database="sales")

# cursor:
# they are bound to the connection for the entire lifetime and all the commands are executed in
# the context of the database session wrapped by the connection.
my_cursor = mydb.cursor()

# creating a db
my_cursor.execute("create database test_db")

# creating tables
my_cursor.execute("create table person(personId int primary key auto_increment, name varchar(20), age smallint unsigned)")






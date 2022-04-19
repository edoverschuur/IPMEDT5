import serial
import os
import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="laravel",
    passwd="123456",
    database="communication"
)

mycursor = mydb.cursor()

mycursor.execute("UPDATE count SET amount = amount + 1")
mydb.commit()


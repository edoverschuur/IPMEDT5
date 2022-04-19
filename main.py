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

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)

while True:
    mycursor.execute("SELECT * FROM led;")
    for x in mycursor:
        print(x[3])
        if x[3] == "aan":
            print(x[3])
            port.write("l1".encode())
        else:
            port.write("l0".encode())


    rcv = str(port.readline().decode().strip()) 
    print(rcv)
    if (rcv == 'bro'):
        import mysql.connector

        mydb = mysql.connector.connect(
                host="localhost",
                user="laravel",
                passwd="123456",
                database="communication"
            )

        mycursor = mydb.cursor()

        mycursor.execute("UPDATE count SET amount = amount + 1;")
        mydb.commit()

        
    
    time.sleep(1)
    mydb.commit()     


mydb.close()
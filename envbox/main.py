import serial
import os
import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="atwin",
    passwd="diegoxdlol",
    database="envbox"
)

mycursor = mydb.cursor()
port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)

while True:
    rcv = str(port.readline().decode().strip()) 
    if (rcv != None):
        time.sleep(2)
        rcv = str(port.readline().decode().strip()) 
        values = rcv.split("/")
        hum = values[0]
        temp = values[1]
        date = int(time.time())

        data = (date,temp,hum)
        
        print(hum)
        print(temp)

        add_data = ("INSERT INTO data "
                "(date, temperature, humidity) "
                "VALUES (%s, %s, %s)")

        mycursor.execute(add_data,data)

        mydb.commit()
    

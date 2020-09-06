import psycopg2
import serial, time
import credentials as cd
from datetime import datetime
from twilio.rest import Client

arduino = serial.Serial('COM3', baudrate=9600, timeout=1)
x = arduino.readline()
x = x.decode("utf-8").strip("\n")

def send_alert():
    client = Client(cd.acc_sid, cd.auth_token)

    message = client.messages.create(
        body="Alert You are violating Social Distancing Rules\nStay Safe",
        from_=cd.from_number,
        to=cd.to_number)

def record():
    con = psycopg2.connect(
        host = "localhost",
        dbname = "devicedata",
        user = "postgres",
        password = "1234"
    )
    cur = con.cursor()
    hrs = datetime.now().hour
    m = datetime.now().minute
    cur.execute("INSERT INTO displaydb (hour, minute) VALUES(%s, %s)",(hrs, m,))
    con.commit()
    cur.execute("SELECT * FROM displaydb")
    print(cur.fetchall())
    print("TimeStamp Recorded")
    con.close()

count = 0
current = datetime.now().minute
temp = 0
while True:
    count+=1
    x = arduino.readline()
    x = x.decode("utf-8").strip("\n")
    x = int(x)
    print(x)
    if(x < 10):
        temp = current
        current = datetime.now().minute
        print("Watch out !! You are violating social distance rules")
        if(temp!=current):
            send_alert()
            record()
    
    time.sleep(0.5)
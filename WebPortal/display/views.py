from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from .models import update_db
import psycopg2

# Create your views here.
def home(request):
    con = psycopg2.connect(
        host="localhost",
        dbname="devicedata",
        user="postgres",
        password="1234"
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM displaydb")
    rows = cur.fetchall()
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for r in rows:
        count[r[0]] +=1

    return render(request, 'index.html', {'my_data':count})
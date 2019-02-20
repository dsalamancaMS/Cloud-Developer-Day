from flask import Flask
from flask import render_template
import os
import pyodbc

app = Flask(__name__)

driver = '{ODBC Driver 17 for SQL Server}'
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

@app.route("/")
def estus_flask():
    cursor.execute("SELECT TOP 5 FirstName, LastName, EmailAddress, Phone FROM SalesLT.Customer")
    data = cursor.fetchall()
    message = "Hello " + os.getenv("HOSTNAME")
    return render_template("index.html", message=message, language="Python")

@app.route("/work")
def memory_load():
    bytearray(512000000)
    message = "Being Monolithic"
    return render_template("gophers_working.html",message=message)
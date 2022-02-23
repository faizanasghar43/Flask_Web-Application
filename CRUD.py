from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pyodbc

carsales = Flask(__name__)
carsales.config


def connection():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-BIC5BPP;"
        "Database=Master;"
        "Trusted_Connection=yes;"
    )
    return conn

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'insert into dbo.TblCars(name,year,price,id) values(?,?,?,?)', ('dogzzz', 3232, 122, 34))
    conn.commit()



def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        'delete from dbo.TblCars where id = 34 '
    )
    conn.commit()

delete(connection())

@carsales.route("/")
def main():
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.TblCars")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
    conn.close()
    return render_template("carlist.html", cars = cars)





if(__name__ == "__main__"):
    carsales.run()
from flask import Flask, render_template
#from conexion import añadiralist
import sys
import pyodbc

#abrir la conexion con la base de datos
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ= c:\Users\cuc\Documents\base\TallerDB.accdb;")
#abrir el cursor
cursor=conn.cursor()
app = Flask(__name__)
@app.route('/')
def index():
    cursor.execute("SELECT * FROM Estudiantes")
    Estudiantes=cursor.fetchall()
    cursor.execute("SELECT * FROM cursos")
    cursos=cursor.fetchall()
    return f"esta es la tabla de estudiantes <br> {Estudiantes} <br> esta es la tabla de cursos <br>{cursos}"
if __name__=='__main__':
    app.run()
cursor.close
#cerrar la conexion
conn.close
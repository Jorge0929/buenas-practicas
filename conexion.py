import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ= C:\Users\jorge\OneDrive\Documentos\universidad\Buenas practicas de desarrollo\Base de datos acces\base_da.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM Estudiante WHERE edad>20")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close






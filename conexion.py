#se importa sys
import sys
#se importa pyodbc para 
import pyodbc
#abrir la conexion con la base de datos
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ= c:\Users\cuc\Documents\base\TallerDB.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM Estudiantes")
lista=[]
def añadiralist():
    for row in cursor.fetchall():
        lista.append(row)
añadiralist()
cursor.close
conn.close
print(lista)





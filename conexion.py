import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ= c:\Users\cuc\Documents\base\Database2.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM persona_1")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close






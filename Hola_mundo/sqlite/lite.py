import os
import sqlite3

def create_table(cur):
    
    sql="drop table if exists people2;"
    
    cur.execute(sql)
    
    sql="""
   CREATE TABLE people2 (
   person_id INTEGER PRIMARY KEY AUTOINCREMENT,
   first_name text NOT NULL,
   last_name text NOT NULL);
   """

    cur.execute(sql)

def inserta_registros(cur):
    
    
    lista=["insert into people2(first_name,last_name) values('Pepe','Perez');",
          "insert into people2(first_name,last_name) values('Juan','Fernandex');",
          "insert into people2(first_name,last_name) values('Miguel','Gonzalez');"
          ]
    
    ok=True
    for i in lista:
        
        try:
            cur.execute(i)
        except:
            print("Registro no insertado")
            ok=False
            break

    return ok

def select_registros(cur):
    
    sql="Select * from people2;"
    cur.execute(sql)
    filas=cur.fetchall()
    
    for i in filas:
        
        print(i[0],i[1],i[2])

def main():
    
    path="..\\..\\sql_lite\\db2"
    conn=sqlite3.connect(path)
    cur=conn.cursor()
    
    create_table(cur)
    
    if inserta_registros(cur):
        conn.commit()
        select_registros(cur)
    else:
        conn.rollback()
        
    
    conn.close()
    
main()
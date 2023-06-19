from os import path,system
import sqlite3

system("cls")

def create_table(cur):
    
    try:
        
        sql="drop table if exists people2;"
        
        cur.execute(sql)
        
        sql="""
    CREATE TABLE people2 (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name text NOT NULL,
    last_name text NOT NULL);
    """

        cur.execute(sql)
        return True
    
    except Exception as e:
        print("Error en la creación de la tabla",e)
        return False

def inserta_registros(cur):
    
    ok=True
    
    try:
        
        lista=["insert into people2(first_name,last_name) values('Pepe','Perez');",
            "insert into people2(first_name,last_name) values('Juan','Fernandex');",
            "insert into people2(first_name,last_name) values('Miguel','Gonzalez');"
            ]
        
        for i in lista:
            
            try:
                cur.execute(i)
            except Exception as e:
                print("Registro no insertado",e)
                ok=False
                break
           
    except Exception as e:
        print("Error en la inserción.",e)
        ok=False
        
    return ok

def select_registros(cur):
    
    try:
        
        sql="Select * from people2;"
        cur.execute(sql)
        filas=cur.fetchall()
        
        for i in filas:
            
            print(i[0],i[1],i[2])
            
    except Exception as e:
        
        print("Error",e)

def delete_registro(cur):
    
    try:
        
        nombre="Pepe"
        sql="delete from people2 where first_name= ?"
        cur.execute(sql,(nombre,))
        return True
    except Exception as e:
        print("No se ha podido borrar el registro",e)
        return False
        
def update_registro(cur):
    
    try:
        
        nombre="Juan"
        nombre2="Pepe"
        sql="update people2 set first_name=? where first_name= ?"
        cur.execute(sql,(nombre2,nombre,))
        return True
    except Exception as e:
        print("No se ha podido actualizar el registro",e)
        return False

        
def main():
    
    db_path="..\\..\\sql_lite\\db2"
    if path.exists(db_path):
        
        try:
            
            conn=sqlite3.connect(db_path)
            cur=conn.cursor()
            
        except Exception as e:
            
            print("Error de conexión",e)
            return
        
        ok=create_table(cur)
        
        if ok:
            ok=inserta_registros(cur)
            select_registros(cur) 
        if ok:
            ok=delete_registro(cur)
            select_registros(cur)
        if ok:
            ok=update_registro(cur)
            select_registros(cur)
        if ok:
            conn.commit()
        else:
            conn.rollback()
            
        conn.close()
    else:
        
        print("Ruta no encontrada",path.abspath(db_path))
    
main()
import os
from conexion import *

os.system("cls")

if __name__=="__main__":
    
    con=Conexion("root","","instituto")
    id=input("Introduzca la Id a buscar")
    con.consulta(id)
    print(con.getMsgError())
    con=None
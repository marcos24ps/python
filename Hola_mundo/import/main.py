from importada import *
import os


os.system("cls")

def entrada():
    
    alumnos=[{"id":"A-1","nombre":"Pepe","nota":6.25},
                {"id":"A-2","nombre":"Juan","nota":3.00},
                {"id":"A-3","nombre":"Lucas","nota":9.75},
                {"id":"A-4","nombre":"Andres","nota":1.00}
                ]
     
    d=Diccionario(alumnos) 
    mensaje="No se ha podido añadir el registro."
    
    if d.add("A-5","Jose",5)==True:
        mensaje="Registro añadido"
       
    print(mensaje)
    ok=d.rango("A-2","A-4")
    msg="No se ha podido eliminar el registro"
    
    if d.eliminar_por_id("A-2")==True:
        mensaje="Registro eliminado"
    
    print(mensaje)
    
    if ok==True:
        d.print(True)
        print("------------------------")
        d.print(False)


entrada()


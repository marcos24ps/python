from importada import *
import os


os.system("cls")

def inicialize():
    
    alumnos=[{"id":"A-1","nombre":"Pepe","nota":6.25},
                {"id":"A-2","nombre":"Juan","nota":3.00},
                {"id":"A-3","nombre":"Lucas","nota":9.75},
                {"id":"A-4","nombre":"Andres","nota":1.00}
                ]
    
    return alumnos

def add(d):
    
    mensaje="No se ha podido añadir el registro."
    id=input("Introduzca el ID")
    nombre=input("introduzca el nombre")
    nota=input("Introduzca la nota")
    
    if d.add(id,nombre,nota)==True:
        mensaje="Registro añadido"
       
    return mensaje

def remove(d):
    
    msg="No se ha podido eliminar el registro"
    id=input("Introduzca el ID")
    
    if d.eliminar_por_id(id)==True:
        mensaje="Registro eliminado"
    
    return mensaje

def modificar(d):
    
    msg="No se ha podido modificar el registro"
    id=input("Introduzca el ID")
    nota=input("Introduzca la nota")
    
    if d.modificar(id,nota)==True:
        mensaje="Registro modificado"
    
    return mensaje
    
def entrada():
    
    alumnos=inicialize()
    mensaje=None
    dic=Diccionario(alumnos)
    
    while True:
        
        print("Elija una opción.")
        print("1. Añadir registro.")
        print("2. Eliminar registro.")
        print("3. Modificar registro.")
        print("4. Mostrar rango.")
        print("6. Mostrar todos los registros.")
        print("7. Salir.")
        
        op=input("Introduzca una opción")
        op=int(op) if op.isdigit() else -1
        
        if op==7:
            break
        elif op==1:
            mensaje=add(dic)
        elif op==2:
            mensaje=remove(dic)
        elif op==3:
            mensaje=modificar(dic)
        else:
            mensaje="Opción errónea"
        
        print(mensaje)

entrada()



def entrada2():
    
    
     
    d=Diccionario(alumnos) 
    
    ok=d.rango("A-2","A-4")
    
    
    if ok==True:
        d.print(True)
        print("------------------------")
        d.print(False)






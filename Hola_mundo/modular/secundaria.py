

def entrada():

    alumnos=[{"id":1,"nombre":"Pepe","nota":6.25},
             {"id":2,"nombre":"Juan","nota":3.00},
             {"id":3,"nombre":"Lucas","nota":9.75},
             {"id":4,"nombre":"Andres","nota":1.00}
            ]
    

    while True:

        op="\n 1. Añadir. \n 2. Borrar Registro. \n 3. Buscar en rango. \n 4. Mostrar registros. \n 5. Modificar. \n 6. Salir \n"
        o=input(op)
        
        if o.isdigit():
            
            o=int(o)
            if o==1:                
                add(input("Introduzca el nombre"),input("Introduzca la nota"),alumnos)
            if o==2:
                o=input("Introduzca el Id")
                delete(o,alumnos)
                mostrar(alumnos)
            if o==3:
                o=buscar_rango(input("Introduzca rango inicio"),input("Introduzca rango fin"),alumnos)
            if o==4:
                mostrar(alumnos)
            if o==5:
                modificar(input("Introduzca el nombre a modificar"),input("Introduzca la nueva nota"),alumnos)
            if o==6:
                break

def add(nombre,nota,alumnos):
    
    id=len(alumnos) + 1   
    alumnos.append({"id":id,"nombre":nombre,"nota":nota})


def delete(id,alumnos):
    
    if id.isdigit():
        
        idd=int(id)
        
        for i,j in enumerate(alumnos):
            
            if j.get("id")==idd:
                
                del alumnos[i]
                break
        

def mostrar(alumnos):
    
    for i in alumnos:
        
        print(i)
        
def buscar_rango(inicio,fin,alumnos):
    
    lista=[]
    
    for i in alumnos:
        
        if i["id"]>=int(inicio) and i["id"]<=int(fin):
            lista.append({"id":i["id"],"nombre":i["nombre"],"nota":i["nota"]})
    
    alumnos=lista

def modificar(nombre,nota,alumnos):
    
    id=-1
    
    for i in alumnos:
        
        if i["nombre"].lower()==nombre.lower():
            
            id=i["id"] -1
            alumnos[id]["nota"]=nota
            break
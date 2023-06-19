import re


class Diccionario:

    
    def __init__(self,arr):
        self.__arr=arr
        self.__busqueda=None
        
    def __validar_formato(self,valorE):
        
        patron="^(A-)[0-9]+"
                
        if re.fullmatch(patron,valorE):
        
            a=re.sub("A-","",valorE)
            
            if  a.isdigit():
                
                return int(a)

        
        return -999

    def __buscar(self,id,nombre):
        
        ret=False
        
        for i in self.__arr:
            
            if id in i["id"] or nombre in i["nombre"]:
                ret=True
                break
        return ret
            
    def rango(self,rangoI,rangoF):
        
        ret=False
        self.__busqueda=None
        
        a=self.__validar_formato(rangoI)
        b=self.__validar_formato(rangoF)
        
        if (a!=-999 and b!=-999) and (b>a):
            
            self.__busqueda=[]
            start=False
            
            for i in self.__arr:
            
                if re.fullmatch(i["id"],rangoI):
                    start=True
                
                if start:
                    self.__busqueda.append(i)
                    ret=True
                
                if re.fullmatch(i["id"],rangoF):
                    break
                
        return ret
                   
        
    def print(self,esBusqueda=False):
        
        arr=self.__busqueda if esBusqueda==True else self.__arr
        
        for i in arr:
            
            print(i)

    def add(self,id,nombre,nota):
        
        ret=False
        if self.__buscar(id,nombre)==False and self.__validar_formato(id)!=-999:
  
            if isinstance(nota,float):
                nota=float(nota)
                self.__arr.append({"id":id,"nombre":nombre,"nota":nota})
                ret= True
        
        return ret
    
    def eliminar_por_id(self,id):
        
        ret=False
        if  self.__validar_formato(id)!=-999:

            for i,j in enumerate(self.__arr):
                
                if id in j["id"]:
                    
                    del self.__arr[i]
                    ret=True
                    break
            
        return ret
    
    def modificar(self,id,nota):
        
        ret=False
        if  self.__validar_formato(id)!=-999:

            for i,j in enumerate(self.__arr):
                
                if id in j["id"]:
                    
                    self.__arr[i]["nota"]=nota
                    ret=True
                    break
            
        return ret



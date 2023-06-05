import os

os.system("cls")


class padre():
    
    __nombre=None
    __edad=None
    __telefono=None
    __contador=None

    def __init__(self,nombre,edad,telefono):
        
        self.__nombre=nombre
        self.__edad=edad
        self.__telefono=telefono
        self.__contador =0
        
        
    def __privado(self):
        
        self.__contador +=1

    def _protegido(self):
        
        self.__privado()
    
    def _sobreEscrito(self,contador):
        
        self.__contador =contador * 100
        return self.__contador
        
        
    def publico(self,cont):
        
        self.__contador=cont
        
        
class hija(padre):
    
    def __init__(self,nombre,edad,rtelefono):
        
        padre.__init__(self,nombre,edad,rtelefono)
        padre._protegido(self)
        

    def _sobreEscrito(self,contador):
        
        cont=padre._sobreEscrito(self,contador)
        cont *=500
        return cont        

if __name__=="__main__":
    
        cHija=hija("Marcos",45,672541680)
        cont=cHija._sobreEscrito(5)
        
        print(cont)
        

import os
import re
from collections import Counter

os.system("cls")

#recorrer cadena por elemento
def elemento():
    
    cadena="hola mundo"
    
    for i in cadena:
        
        print(i,end=" ")

#recorrer por indice

def indice():
    
    cadena="hola mundo"
    for i in range(len(cadena)):
        
        print(cadena[i],end=" ")

#Recorrer por enumerador
def enumerador():
    
    cadena="hola mundo"
    for i,e in enumerate(cadena):
         
        print((i,e),end=" ")
        
#Recorrer por lista.       
def lista():
    
    cadena=list("hola mundo")
    
    for i in cadena:
        
        print(i,end=" ")

#rango cadena

#subcadenas
def subcadena():
    
    cadena="hola mundo esto es una prueba"
    res=cadena[5:6:1] #inicio,fin,contador
    res1=cadena[::-1] #reverso cadena
    res2=cadena[5:4:-1] #fin, inicio, contador
    
    print(res)
    print(res1)
    print(res2)

def reves():
    
    cadena="hola esto es una prueba"
    cadena2=""
    
    i=range(len(cadena))
    
    for i in range(len(cadena) -1,-1,-1):
        
        cadena2 +=cadena[i]
    
    print(cadena2)
     
def reves2():
    
    cadena="hola esto es una prueba"
    cadena2=""
    
    for i in cadena:
        
        cadena2=i + cadena2
    
    print(cadena2)
        
def remplazar_col():
    
    cadena="hola esto es una prueba"
    pattern="[aeiouáéíóú]"
    
    cadena=cadena.lower()
    lista=list(cadena)
    
    for i,j in enumerate(cadena):
        
        if re.fullmatch(pattern,j):
            lista[i]="X"
        
        cadena=str(lista) 
    
    print(cadena)
        
def replace_sub():
    
         cadena="hola esto es una prueba"
         pattern="[aeiouáéíóú]"
         cadena2=re.sub(pattern,'X',cadena)
         
         print(cadena2)

def replace_sub_num():
    
         cadena="h0la est1 es un3 pru2ba"
         pattern="[0-9]"
         cadena2=re.sub(pattern,"",cadena)
         
         print(cadena2)

def sub():
    
    cadena=input("Introduzca la primera cadena")
    cadena2=input("Introduzca la subcadena")
    
    cadena=list("hola esto es una prueba")
    cont=0
    c=""
    
    for i in cadena2:
        
     
        if re.fullmatch(i,cadena[cont]):
            c=c + " " + i
            print("Coincide",c)
            cont +=1
        else:
            print ("No coinciden")
            break
    
    re.search("^" + cadena2,cadena) 
 
 
 #Contar no repetidos y mostrar repetidos y veces
def pruebadd():

    array="Hola mundo prueba mundo adios"
    arr={}
    
    array=array.split(" ")
    
    for i in array:
        
        resul=[]
        if(i  not in arr):
            resul.append(1)
            arr[i]=resul          
        else:
            resul=arr[i]
            resul[0] +=1            
            arr[i]=resul
            
    print(arr)
   
if __name__=="__main__":
    
    #elemento()
    ##indice()
    ##enumerador()
    ##lista()
    ##subcadena()
    #reves()
    #reves2()
    #remplazar_col()
    #replace_sub
    #replace_sub_num()
    #sub()
    pruebadd()
    




    
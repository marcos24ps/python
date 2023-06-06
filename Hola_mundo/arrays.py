import os

os.system("cls")

if __name__=="__main__":
    
    #Declaracion array estatico
    lista=[0] * 3
    lista[0]=1
    lista[1]=2
    lista[2]=3
    
    
    #foreach
    for e in lista:
        print(e)
        
        
    #declaracion array dinamico
    listab=[]
    listab.append(1)
    listab.append(2)
    listab.append(3)

    #foreach
    for ee in listab:
            print(ee,end=" ")
       
    print(end="\n")
    
    #for normal.
    for x in range(len(lista)):
        print(lista[x],end=" ")
        
        
   #eliminar por valor
   
    listab.remove(0) #Elimina el primer cero que encuentre.
    
    for x in listab:
        print("Lista b",x)
 
 #Eliminar por indice.
    
    
    del listab[1]
     
#eliminar por elemento.


    listab.pop(1)
    
    

vector=[1,2,3,4,5,6,7,8,9]
vector_par=[]
vector_impar=[]

for el in vector_par:
    if el %2 == 0:
        vector_par.append(el)
    else:
        vector_impar.append(el)
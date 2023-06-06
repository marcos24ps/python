import os

os.system("cls")

if __name__=="__main__":
    
    arr=[1,2,3,4,2]
    
    lista={*arr} #ãñadir un array a campoon a una lista. Los repetidos, no los añade.
    prueba=set() #definicion
    
    for itm in lista:
        
        print(itm)


#Eliminar.

lista.remove(2) #limpiar elemento 2

for a in lista:
    
    print(a)
    
lista.clear() #Limpiar todos
print(lista)


lista={*arr}
os.system("cls")

for i in range(len(lista)):

    print(i)
    if  i!=2:
        print("elimino")
        lista.pop()


for i in lista:
    print("valor: ",i)
    

a={1,2,3,4}
b={2,4,5,3}

c= a & b #Elementos en comun

print("Elementos en comun",c)

c=a|b

print("Todos elementos dos conjuntos",c) #Todos elementos dos conjuntos.

c=a-b 

print("Pertenezcan a a y no b",c) #Pertenezcan a a y no b


c=b>=a #B incluye a a

print ("B incluye a a",c)

a={1,2,3}
b={3,2,1}

c=b>=a #B incluye a a

print ("B incluye a a",c)

c=a.isdisjoint(b)

print("No elementos comun",c)

a={1,2,3}
b={4,5,6}

c=a.isdisjoint(b)

print("No elementos comun",c)
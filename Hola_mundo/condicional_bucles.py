import os

os.system("cls")

a=9
b="Es menor"

if(a>=98):
   b="es mayor"

print(b)

#if anidados

if(a<5):
    b="Suspenso"
elif(a>5):
    print("Aprobado")

a=0
while(a<5):
    print("valor: ",a)
    a+=1
    

j=int(input("ingrese un valor"))


for i in range(j):
    print (i, end=" ")
    
 
for i in range(1,j +1,1):
    print (i, end=" ")
    
for i in range(j,0,-1):
    print (i, end=" ")
    

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


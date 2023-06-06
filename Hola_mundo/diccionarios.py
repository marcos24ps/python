import os

os.system("cls")

#Definicion estática.
dic={"Marcos":"uno",
     "Edad":22,
     "Estatura":1.75
     }

#Sacar clave y valor.
for i,j in enumerate(dic):
    
    print(i,j)
    

arr=["a","b","c"]


os.system("cls")  


for i,j,k in zip(arr,enumerate(dic)):
   
   texto=i + " " + j + " " +k 
   print(texto)

"""
os.system("cls")  


print("Busqueda por clave",dic.get("Marcos"))
"""

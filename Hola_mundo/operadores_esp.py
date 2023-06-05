vector=[1,2,3,4,1,2,4,3,9]
resultado=[]




for el in vector:
    if el not in resultado:
        resultado.append(el)


try:

    cont=vector.index(1) # IndexOf de javascript
    cont1=vector.count(1) #contador de cuantas veces está el 1 en el array.
except Exception as e:
    print(e)
    cont=-1


print(cont)

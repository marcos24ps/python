

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            return False
    return True

n=input("Introduce un numero del uno al 20")
if n.isdigit():
    
    n=int(n)
    arr=[]
    
for num in range(1, n):
    if es_primo(num):
        arr.append(num)
        

for nx in arr:

    print(nx)
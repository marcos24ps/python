import os

os.system("cls")

#ej datos
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"


datos=datos_clientes.split("\n")
lista={}
arr=[]

for i in datos:
      
   arr.append(i.split(";"))


cont=0
for j in arr:
    
    if j==0:
        
        print('%-6s %-6s %6s %-6s %-6s' % (j[0],j[1],j[2],j[3],j[4]))
        print('%-6s %-6s %6s %-6s %-6s' % ('------','------','----','--------','------'))
    else:
        print('%-6s %-6s %6s %-6s %-6s' % (j[0],j[1],j[2],j[3],j[4]))


os.system("cls")


#Ej 1

l={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

i=input("Introduzca la divisa")

if i in l:
    
    print("Su divisa es",l[i])
else:
    print("Divisa no encontrada")
    

os.system("cls")

#ej 2

nom=input("Introduzca su nombre")
ed=input("Introduzca su edad")
dir=input("Introduzca su direccion")

arr={"Nombre":nom,"Edad":ed,"Dir":dir}
print("Su nombre es:",arr["Nombre"])
print("Tiene:",arr["Edad"])
print("Vive en:",arr["Dir"])

#ej 3


frutas={
        "Plátano":{"precio":1.35},
        "Manzana":{"precio":0.80},
        "Pera":{"precio":0.85},
        "Naranja":{"precio":0.70}
        }

f=input("Introduzca la fruta.")

if f in frutas:

    k=input("Introzuca el número de kilos")
        
    if k.isdigit():
        
        precio=frutas[f]["precio"] * int(k)
        print(f"El precio de {f}, es {precio} euros")
    else:
        
        print("Valor erróneo para el número de kilos.")
else:
    print(f"Fruta {f}, no encontrada")
    

#ej 4


s=input("Introduzca una fecha en formato dd\MM\yyyy")

mensaje="Formato de fecha errónea"

f=s.split("\\")
 
if  len(f)==3:
    
    dia= int(f[0]) if f[0].isdigit() else None
    mes= int(f[1]) if f[1].isdigit() else None
    ano= int(f[2]) if f[2].isdigit() else None
    mes -=1
    anos=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","nobiembre","diciembre"]
    mensaje=f"{dia} de {anos[mes]} de {ano}"
          
print(mensaje)

#ej 5

d={'Matemáticas': 6, 'Física': 4, 'Química': 5}

for i,j in enumerate(d):
    
    print("La asignatura: ",j,"Tiene",d[j],"Créditos")

#ej 6
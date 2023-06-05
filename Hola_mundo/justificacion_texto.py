#justificacion

codigos=[1,2,3,4]
nombres=["Marcos","pepe","Luis","Carlos"]
edad=[15,19,22,44]
estatura=[1.66,1.44,1.57,1.76]
casado=["N","N","S","S"]

print('%-5s %-6s %4s %-8s %-6s' % ('Codigo','Nombre','Edad','Estatura','Casado'))
print('%-5s %-6s %4s %-8s %-6s' % ('------','------','----','--------','------'))

for i in range(len(codigos)):
    print('%-5d %-6s %4d %-8.2f %-6s' % (codigos[i],nombres[i],edad[i],estatura[i],casado[i]))
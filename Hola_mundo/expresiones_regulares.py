import os
import re

os.system("cls")

patron="[0-9]+"
patronn="^[\.][a-z A-Z 0-9]"
while True:
    
    res=input("Ingrese el valor")
    if re.fullmatch(patron,res):
        break
        

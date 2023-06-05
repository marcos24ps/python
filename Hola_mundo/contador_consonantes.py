
arr=list("En un lugar de la mancha".lower())
voc=['a','e','i','o','u','á','é','í','ó','ú']

cont=0

for i in range(len(voc)):
    cont +=arr.count(voc[i])



print(cont)



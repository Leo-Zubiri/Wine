
from KNN_Wine import KNN

resultados=[]


with open("resultados.csv", "w") as f:
    lista=["        K"," Rendimiento"," Aciertos"]
    for el in lista:
        f.write('{},'.format(el))
    f.write("\n")



for k in range(1,36,1):
    res = KNN(k)
    resultados.append(res)
    with open("resultados.csv", "a") as f:
        lista=["K","Rendimiento","Aciertos"]
        for el in res:
            f.write('{},'.format(el))
        f.write("\n")


rends = [x[1] for x in resultados]
mayRend = max(rends)

print("\n\nK","Rendimiento","Aciertos")
for el in resultados:
    if el[1]==mayRend:
        print(el)

print(mayRend)































'''
Toma de vectores aleatorios

cantidad = len(instancia) / 5
centroides = []
while len(centroides) < int(cantidadClusters):
    vector = instancia[randint(0, 1000)]
    if vector in centroides:
        vector = instancia[randint(0, 1000)]
    else:
        centroides.append(vector)
'''
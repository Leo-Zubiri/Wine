from random import shuffle
# Si quieres usa mi unpack de KNN_Y 😉
archivo = open("Instancia_wine.csv","r")
    #archivo = open("iris_prueba.csv","r")
contenido = archivo.readlines()

lista = [linea.split(",") for linea in contenido]

valores = [ [ list(map(float,x[:13])), int(x[13].replace("\n","")) ] for x in lista ] 
archivo.close()

shuffle(valores)

with open("wine_entrenamiento.csv", "w") as f:
    for i in range(125):
        for j in valores[i][0]:
            f.write('{},'.format(j))
        f.write('{}'.format(valores[i][1]))
        f.write("\n")

with open("wine_prueba.csv", "w") as f:
    for i in range(125, len(valores), 1):
        for j in valores[i][0]:
            f.write('{},'.format(j))
        f.write('{}'.format(valores[i][1]))
        f.write("\n")

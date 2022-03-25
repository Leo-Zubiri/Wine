
from KNN import KNN

nomMets = ["Manhattan","Euclidiana","Euclidiana_norm","Jaccard","Coseno","Sorence_Dice"]
testFiles = ["wine_test60.0.csv","wine_test70.0.csv","wine_test80.0.csv","wine_test90.0.csv"]
trainingFiles = ["wine_training60.0.csv","wine_training70.0.csv","wine_training80.0.csv","wine_training90.0.csv"]

metricas = [0,1]
testFiles = ["wine_test60.0.csv","wine_test70.0.csv","wine_test80.0.csv","wine_test90.0.csv"]
trainingFiles = ["wine_training60.0.csv","wine_training70.0.csv","wine_training80.0.csv","wine_training90.0.csv"]


with open("resultados.csv", "w") as f:
    lista=["        K"," Rendimiento"," Aciertos"]
    for el in lista:
        f.write('{},'.format(el))
    f.write("\n")

for archivo in range(len(testFiles)):
    testFile = open(testFiles[archivo])
    trainingFile = open(trainingFiles[archivo])

    testContent = testFile.readlines()
    trainContent = trainingFile.readlines()

    lista = [linea.split(",") for linea in testContent]
    test = [ [ list(map(float,x[:len(lista[0])-1])), int(x[len(lista[0])-1].replace("\n","")) ] for x in lista ]

    lista = [linea.split(",") for linea in trainContent]
    training = [ [ list(map(float,x[:len(lista[0])-1])), int(x[len(lista[0])-1].replace("\n","")) ] for x in lista ]


    for metrica in metricas:
        print('\n**** Metrica: {} Archivo: {} *****,'.format(nomMets[metrica],testFiles[archivo]))
        with open("resultados.csv", "a") as f:
            f.write('**** Metrica: {} Archivo: {} *****,'.format(nomMets[metrica],testFiles[archivo]))
            f.write("\n")
        for k in range(1,len(testContent)+1,1):
            data = KNN(k,test,training,metrica)
            with open("resultados.csv", "a") as f:
                for el in data:
                    f.write('{},'.format(el))
                f.write("\n")


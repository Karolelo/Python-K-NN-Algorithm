import pandas as pd

def euclidesLenght(vector1, vector2):
    lenght=0
    for i_1, i_2 in zip(vector1, vector2):
        lenght+=(i_1-i_2)**2
    return lenght**0.5

def readTrainingFile(file_name):

    df = pd.read_csv(file_name, delimiter=';')

    return df.values.tolist()

def readTestFile(file_name):

    df = pd.read_csv(file_name, delimiter=';')

    return df.iloc[:, :-1].values.tolist()

list=readTrainingFile("C:\\Users\\48509\\Desktop\\iris.csv")

##trainingFilePath = input("Give path to training file :")

##testFilePath = input("Give path to test file :")

k = input("Give k")

##vectors = readTrainingFile(trainingFilePath)

##Creating map of vectors

mapa = {}
for listOfList in list:
        key = listOfList[-1]
        value = listOfList[:-1]
        if key in mapa.keys():
            mapa[key]+=value
        else:
            mapa[key] = [value]


##vectorsToClassified = readTestFile(testFilePath)

closestVec = [];


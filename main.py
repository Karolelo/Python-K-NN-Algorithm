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

    df = pd.read_csv(file_name, delimiter=';')

    return df.iloc[:,:-1].values.tolist()

trainingList=readTrainingFile("C:\\Users\\48509\\Desktop\\iris.csv")
testList=readTestFile("C:\\Users\\48509\Desktop\\TestFile.csv")
##trainingFilePath = input("Give path to training file :")

##testFilePath = input("Give path to test file :")


##vectors = readTrainingFile(trainingFilePath)

##Creating map of vectors
def create_map_ofTraingFIle(trainingList):
    mapa = {}
    for listOfList in trainingList:
            key = listOfList[-1]
            value = listOfList[:-1]
            if key in mapa.keys():
                mapa[key].append(value)
            else:
                mapa[key] = [value]
    return mapa


##vectorsToClassified = readTestFile(testFilePath)
exampleVec=[1,3,4,4]



def k_nearest_neighbors(mapa, exampleVec, k):
    closestVec = []
    for key, values in mapa.items():
        for value in values:
            distance = euclidesLenght(exampleVec, value)
            closestVec.append((key, distance))

    closestVec.sort(key=lambda x: x[1])

    return closestVec[:k]

print(testList)
for testingData in testList:
    k_nearest_neighbors(mapa,testingData,3)


    ##TODO zmienić funkcje do czytania tego gówna
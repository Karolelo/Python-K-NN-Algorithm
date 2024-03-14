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

trainingList=readTrainingFile("C:\\Users\\48509\\Desktop\\TestFile.csv")
testList=readTestFile("C:\\Users\\48509\Desktop\\traingFile.csv")

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




def k_nearest_neighbors(mapa, exampleVec, k):
    closestVec = []
    for key, values in mapa.items():
        for value in values:
            distance = euclidesLenght(exampleVec, value)
            closestVec.append((key, distance))

    closestVec.sort(key=lambda x: x[1])

    return closestVec[:k]



mapa=create_map_ofTraingFIle(trainingList)

for data in testList:
    closestVec = k_nearest_neighbors(mapa,data,3)
    countedValues={}
    for eachOne in closestVec:
        key=eachOne[0]
        value=eachOne[1]
        if key in countedValues.keys():
            countedValues[key]+=1
        else:
            countedValues[key]=1

    maxOccurence = 0
    mostCommonKey = None

    for key,value in countedValues.items():
        if value > maxOccurence:
            mostCommonKey=key
            maxOccurence=value
    print(f"{data} closest vectors to this {mostCommonKey}")



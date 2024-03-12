import pandas as pd
vectors = []


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


trainingFilePath = input("Give path to training file :")

testFilePath = input("Give path to test file :")
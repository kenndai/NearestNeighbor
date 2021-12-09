import random

def forwardSearch(openFile):
    features = []

    print("\nBeginning search!")

    for i in range(getNumColumns(openFile) - 1):
        level = i + 1
        bestFeature = -1
        bestAcc = -1
        print(f"On level {level} of the search tree")

        for j in range(getNumColumns(openFile) - 1):

            featureNum = j + 1
            # check if the current feature is in the features 
            if (featureNum not in features): 
                print(f"--Considering adding feature {featureNum}")
                featureAcc = crossValidation()

                # compare the accuracy for the current feature
                if (featureAcc > bestAcc):
                    bestAcc = featureAcc
                    bestFeature = featureNum
        
        features.append(bestFeature)
        print(f"On level {level}, feature {bestFeature} was added!\n")
    
    print(features)
    return features

def crossValidation():
    return random.randint(0, 10)

def getNumColumns(openFile):
    line = openFile.readline().strip()
    return len(line.split())

def getColumn(openFile, colNum):
    lines = openFile.readlines()
    result = []
    for line in lines:
        result.append(line.split()[colNum].strip())
    return result

def main():
    print("Welcome to the Feature Selection Algorithm")
    userFile = input("Type in the name of the file to test: \n")

    file = open(userFile, "r")
    
    # print(getColumn(file, 1))
    # print(getNumColumns(file))
    forwardSearch(file)

    file.close()

main()
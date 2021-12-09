import random
import numpy as np

def forwardSearch(file):
    with open(file, "r") as openFile:
        numColumns = getNumColumns(openFile) - 1
        openFile.seek(0)
        features = []

        for i in range(numColumns):
            level = i + 1
            bestFeature = -1
            bestAcc = -1
            print(f"On level {level} of the search tree")

            for j in range(numColumns):

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
    openFile.close()

    print(features)
    return features

def accuracy(file):
    with open(file, "r") as openFile:
        numRows = getNumRows(openFile)
        openFile.seek(0)

        for i in range(numRows):
            iLine = openFile.readline()
            iObject = [float(item) for item in iLine.strip().split()]
            label = int(iObject.pop(0))
            savedPosition = openFile.tell()

            nnDistance = float("inf")
            nnLocation = float("inf")
            nnLabel = ""

            openFile.seek(0)
            for j, jLine in enumerate(openFile):
                if j != i:
                    jObject = [float(item) for item in jLine.strip().split()]
                    jObject.pop(0)

                    # distance = sqrt of the sum of the difference squared
                    distance = np.sqrt(np.sum(np.square(np.asarray(iObject) - np.asarray(jObject))))
                    if distance < nnDistance:
                        nnDistance = distance
                        nnLocation = j + 1 
                        # nnLabel = label of nnLocation

            # restore the file position for the next i iteration
            openFile.seek(savedPosition)
    openFile.close()

def crossValidation():
    return random.randint(0, 10)

def getNumRows(openFile):
    lines = openFile.readlines()
    numRows = 0
    for line in lines:
        numRows += 1
    return numRows

def getNumColumns(openFile):
    line = openFile.readline().strip()
    return len(line.split())

def main():
    print("Welcome to the Feature Selection Algorithm")
    userFile = input("Type in the name of the file to test: \n")

    print("\nBeginning search!")
    # forwardSearch(userFile)
    accuracy(userFile)

main()
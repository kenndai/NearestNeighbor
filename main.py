import random
import numpy as np

def forwardSearch(data):
    print("\nBeginning forward search!")
    
    numOfFeatures = len(data[0]) - 1

    bestFeatures = []
    bestAccEver = -1
    currentFeatures = []

    for i in range(numOfFeatures):
        level = i + 1
        currBestFeature = -1
        bestAcc = -1
        print(f"On level {level} of the search tree")

        for j in range(numOfFeatures):
            featureNum = j + 1
            # check if the current feature is in the features 
            if featureNum not in currentFeatures: 
                goodFeats = currentFeatures.copy()
                goodFeats.append(featureNum)
                featureAcc = crossValidation(data.copy(), goodFeats)
                print(f"--Using feature(s) {goodFeats} has accuracy {featureAcc}")

                # compare the accuracy for the current feature
                if featureAcc > bestAcc:
                    bestAcc = featureAcc
                    currBestFeature = featureNum

        currentFeatures.append(currBestFeature)

        # compare the accuracy of the current set of features against the best set of features
        if bestAcc > bestAccEver:
            bestAccEver = bestAcc
            bestFeatures = currentFeatures.copy()

        print(f"On level {level}, feature {currBestFeature} was added!\n")

    return bestFeatures

def backwardsElim(data):
    print("\nBeginning backwards elimination!")

    numOfFeatures = len(data[0]) - 1
    bestFeatures = []
    bestAccEver = -1
    currentFeatures = []

    # accumulate all feature numbers into current features
    for i in range(numOfFeatures):
        currentFeatures.append(i + 1)

    # loops through all 10 features 
    for i in range(numOfFeatures):
        level = i + 1
        currBestFeature = -1
        bestAcc = -1

        print(f"On level {level} of the search tree")
        print(f"Current Features: {currentFeatures}")

        # j is looping over the features
        for j in reversed(range(numOfFeatures + 1)):
            # check if j hasn't been eliminated yet
            if j in currentFeatures:
                newFeatures = currentFeatures.copy()
                eliminatedFeature = newFeatures.pop(newFeatures.index(j))
                featureAcc = crossValidation(data, newFeatures) # run cross validation on currentFeatures.copy
                print(f"--Eliminating feature {eliminatedFeature} has accuracy {featureAcc}")
            
                # compare the accuracy for the current feature
                if featureAcc > bestAcc:
                    bestAcc = featureAcc
                    currBestFeature = eliminatedFeature

        # at the end of each i iteration, pop the best element from currentFeatures
        currentFeatures.pop(currentFeatures.index(currBestFeature))
        print(f"At level {level} eliminated feature {currBestFeature}\n")

        # compare the accuracy of the current set of features against the best set of features
        if bestAcc > bestAccEver:
            bestAccEver = bestAcc
            bestFeatures = currentFeatures.copy()

    return bestFeatures

def crossValidation(data, features):
    numRows = len(data)
    goodFeatures = features.copy()
    goodFeatures.insert(0, 0)
    numFeatures = len(goodFeatures)

    # declares a 2d-list and copies the features from data
    cleanedData = [[0 for v in range(numFeatures)] for w in range(numRows)]
    for x in range(numRows):
        for y in range(numFeatures):
            cleanedData[x][y] = data[x][goodFeatures[y]]

    numClassifiedCorrectly = 0

    for i in range(numRows):
        # copy the ith row from cleanedData
        ithRow = cleanedData[i].copy()
        iLabel = int(ithRow.pop(0))

        # initialize nearest neighbor variables
        nnDistance = float("inf")
        nnLabel = ""

        # reset file position to the beginning of the file
        for j in range(numRows):
            if j != i:
                # copy the jth row from cleanedData
                jthRow = cleanedData[j].copy()
                jLabel = int(jthRow.pop(0))

                # distance = sqrt of the sum of the difference squared
                distance = np.sqrt(np.sum(np.square(np.asarray(ithRow) - np.asarray(jthRow))))

                # if the calculated distance is now the smallest, update nearest neighbor variables        
                if distance < nnDistance:
                    nnDistance = distance
                    nnLabel = jLabel

        # if labels match, the object was identified correctly
        if iLabel == nnLabel:
            numClassifiedCorrectly += 1

    accuracy = numClassifiedCorrectly / numRows
    return accuracy

def main():
    print("Welcome to the Feature Selection Algorithm")
    userFile = input("Type in the name of the file to test: \n")

    data = []
    with open(userFile, "r") as openFile:
        for i, line in enumerate(openFile):
            row = [float(item) for item in line.strip().split()]
            data.append(row)
    openFile.close()

    backwardsElim(data)

    # searchChoice = input("Type the number of the algorithm that you'd like to run.\n 1) Forward Selection\n 2) Backward Elimination\n")
    
    # if searchChoice == 1:
    #     print(forwardSearch(data))
    # elif searchChoice == 2:
    #     backwardsElim(data)
    # else:
    #     print(f"Sorry, {searchChoice} is not an option.")
    #     exit(1)

main()
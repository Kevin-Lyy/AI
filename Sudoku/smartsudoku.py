#! /usr/bin/python3

import sys
import copy
import time

input = open(sys.argv[1],"r").read().split("\n")

Cliques=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],
[36,37,38,39,40,41,42,43,44],
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]]

#opens the board in arg 1 using title from arg 2
def getBoard():
    index = input.index(sys.argv[2])
    board = list()
    for line in input[index+1:index+10]:
        row = [value if value == "_" else int(value) for value in line.split(",")]
        board.append(row)

    return board

#creates a dictionary of each box and the three cliques its in
def getcliques():
    newcliques = dict()

    for i in emptyList:
        lstclique = list()
        for clique in Cliques:
            if i in clique:
                lstclique += clique
        newcliques[i] = lstclique

    return newcliques

#creates a dictionary of the possible values of each box
def dictofpossible():
    possibleDict = dict()
    values = [1,2,3,4,5,6,7,8,9]

    for i in emptyList:
        usedNums = set()
        for neighbor in neighborhoodDict[i]:
            r = int(neighbor / 9)
            c = neighbor % 9

            if board[r][c] != "_":
                usedNums.add(board[r][c])

        possibleVal = [x for x in values if x not in usedNums]
        possibleDict[i] = possibleVal

    return possibleDict

board = getBoard()
emptyList = [r * 9 + c for r in range(9) for c in range(9) if board[r][c] == "_"] #list of indices of empty space
neighborhoodDict = getcliques() #dictionary {index : neighborhood}
possibleDict = dictofpossible() #dictionary {index : possibleValues}


def forced():
    global count
    guaranteeList = [key for key in possibleDict if len(possibleDict[key]) == 1]
    if len(guaranteeList) == 0:
        return 0
    for i in guaranteeList:
        r = int(i / 9)
        c = i % 9
        if len(possibleDict[i]) == 0:
            return -1
        board[r][c] = possibleDict[i][0]
        possibleDict.pop(i)
        for neighbor in neighborhoodDict[i]:
            if neighbor in possibleDict:
                possibleVals = possibleDict[neighbor]
                if board[r][c] in possibleVals:
                    possibleVals.remove(board[r][c])
    return 1

def unique():
    possibleListClique =[[num for index in clique if index in possibleDict for num in possibleDict[index]] for clique in Cliques]
    count = [[possibleList.count(i) for i in range(1,10)] for possibleList in possibleListClique]
    uniqueDict = dict()
    for cliqueIndex in range(27):
        for numIndex in range(9):
            if count[cliqueIndex][numIndex] == 1:
                uniqueDict[cliqueIndex] = numIndex + 1
    if len(uniqueDict) == 0:
        return 0
    for key in uniqueDict:
        for index in Cliques[key]:
            if index in possibleDict:
                if uniqueDict[key] in possibleDict[index]:
                    possibleDict.update({index : [uniqueDict[key]]})
    if forced() == -1:
        return -1
    return 1

def findEmpty():
    for key in possibleDict:
        return key
    return None

count = 0
def solve():
    global board
    global possibleDict
    global count
    while True:
        boolean1 = forced()
        boolean2 = unique()
        if boolean1 == -1 or boolean2 == -1:
            count += 1
            return False
        elif boolean1 == 0 and boolean2 == 0:
            break
    index = findEmpty()
    if index is None:
        return True
    r = int(index / 9)
    c = index % 9
    tempBoard = copy.deepcopy(board)
    tempDict = copy.deepcopy(possibleDict)
    for i in possibleDict[index]:
        board[r][c] = i
        possibleDict.pop(index)
        for neighbor in neighborhoodDict[index]:
            if neighbor in possibleDict:
                possibleVals = possibleDict[neighbor]
                if i in possibleVals:
                    possibleVals.remove(i)
        if solve():
            return True
        possibleDict = copy.deepcopy(tempDict)
        board = copy.deepcopy(tempBoard)
        count += 1
    return False

def display():
    start = time.time()
    if solve():
        print (time.time() - start)
        print (count)
        return(board)

display()

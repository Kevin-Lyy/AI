#! /usr/bin/python
import sys

input = open(sys.argv[1],"r").read().split("\n")
output = open(sys.argv[2],"w")

def getBoard():
    index = input.index(sys.argv[3])
    board = list()
    for line in input[index+1:index+10]:
        line = line.split(',')
    	for y in line:
    		board.append(y)
    return board

boards = getBoard()

Cliques=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],\
[36,37,38,39,40,41,42,43,44],\
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],\
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
[60,61,62,69,70,71,78,79,80]\
]

def printboard(board):
    lenb = 0
    temp = []
    while lenb < len(board):
        temp.append(board[lenb])
        if len(temp) == 9:
            print(temp)
            temp = []
        lenb += 1

def checkboard(board,index):
    for clique in Cliques:
        for x in clique:
            if x == index:
                i = 0
                j = 1
                while i < len(clique):
                    while j < len(clique):
                        if board[clique[i]] == board[clique[j]] and board[clique[i]] != '_':
                            return False
                        j += 1
                    i += 1
                    j = i + 1
    return True

def findEmpty():
    for i in range(len(boards)):
        if boards[i] == "_":
            return i
    return None

def sudoku():
    box = findEmpty()
    if box is None:
        #if board is filled
        #index = sys.argv[3].index("unsolved")
        #output.write(sys.argv[3][:index] + sys.argv[3][index + 2:] + '\n')
        x = 0
        temp =[]
        while x < len(boards):
            temp.append(boards[x])
            if len(temp) == 9:
                for y in temp:
                    output.write(y)
                    if(y == temp[len(temp)-1]):
                        output.write('\n')
                    else:
                        output.write(',')
                temp = []
            x +=1
        return boards
    else:
        #looks through options of spot
        for num in range(1,10):
            boards[box] = str(num) #places number into board
            if(checkboard(boards,box) == True): #if placement works -> recursion
                sudoku()
        boards[box] = "_" #if all options failed, replace number with "_" and backtrack
        return False

#485
#35172
#49582

sudoku()

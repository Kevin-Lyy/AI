#! /usr/bin/python
import sys

with open("boards.txt","r") as r:
    temp = r.read().split('\n')

nums = [1,2,3,4,5,6,7,8,9]
boards = []
for x in temp:
	x = x.split(',')
	for y in x:
		boards.append(y)
boards = boards[:-1]

tracker = [0] * len(boards)
def cleantracker(board):
    t = 0
    while t < len(boards):
        if(boards[t] == '_'):
            pass
        else:
            tracker[t] = -1
        t += 1

cleantracker(boards)

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
            #print('\n')
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

def forced():
    box = 0
    ftrack = 0
    while box < len(boards):
        if tracker[box] != -1:
            num = 0
            temp = []
            while num < len(nums):
                boards[box] = str(nums[num])

                if(checkboard(boards,box) == True):
                    temp.append(nums[num])

                if(len(temp) == 1):
                    boards[box] = str(temp[0])
                    ftrack +=1
                else:
                    boards[box] = '_'

                num += 1

            tracker[box] = temp
        box += 1
        cleantracker(boards)
    return ftrack

def sudoku():
    x = forced()
    y = forced()
    while(x != forced()):
        x = forced()

    box = 0
    backtrack = 0

    while box < len(boards):
        if tracker[box] != -1:

            if backtrack == 0:
                num = 0
            else:
                #how do i go to the next available option
                #infinite loop when backtracking and setting
                #the value to the same
                box -= 2
                while tracker[box] > 0:
                    if tracker[box] != -1:
                        num = backtrack
                        break
                    box -= 1

            #looks through options of spot
            while num < len(tracker[box]):
                boards[box] = str(tracker[box][num])

                if(checkboard(boards,box) == True):
                    #breks and moves on board placement
                    backtrack = 0
                    break

                if(checkboard(boards,box) == False):
                    #look through the next numbers in nums
                    boards[box] = '_'
                    num += 1

                if(num == len(tracker[box])):
                    #no number works, sets up backtrack
                    boards[box] = '_'
                    #backtrack += 1

        box += 1



printboard(boards)
#sudoku()
print('\n')
printboard(tracker)
print('\n')
#printboard(tracker)
printboard(boards)

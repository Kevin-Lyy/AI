from heapq import heappush, heappop
import sys


wordList = open("dictall.txt","r").read().split()
length = 4
lengthSet = set([x for x in wordList if len(x) == length])
dictionary = dict()

for word in lengthSet:
        outList = []
        for position in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:position] + char + word[position + 1:]
                if newWord != word and newWord in lengthSet:
                    outList.append(newWord)
        dictionary[word] = outList

def getCost(currWord, targetWord):
    counter = 0
    for i in range(len(targetWord)):
        if targetWord[i] != currWord[i]:
            counter += 1
    return counter

def wordLadder(start,target):
    path = []
    currNeighbors = [start]
    while True:
        for neighbor in currNeighbors:
            heappush(frontier,[getCost(neighbor,target)+len(path),neighbor,path])
        if len(frontier) == 0:
            return [start,target]            
        frontierNode = heappop(frontier)
        if frontierNode[1] == target:
            retVal = frontierNode[2] + [frontierNode[1]]
            return retVal
        else:
            if frontierNode[1] not in explored:
                explored.add(frontierNode[1])
                path = frontierNode[2] + [frontierNode[1]]
                currNeighbors = [word for word in dictionary[frontierNode[1]] if word not in explored]                
            else:
                path = []
                currNeighbors = []
                
def wordLadderList()
input = open(sys.argv[1],"r").read().split()
output = open(sys.argv[2],"w")
for wordPair in input:
    

input = (("head","tail"),("hate","love"),("read","head"),("hazy","frog"),("head","ache"))
for pair in input:
    frontier = []
    explored = set()
    print(wordLadder(pair[0],pair[1]))

# frontier = PQueue(is_min=True, compare=CompareCost, startlist=[])
# explored = set()
# print(wordLadder("hazy","frog"))



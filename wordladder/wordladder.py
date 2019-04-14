#! /usr/bin/python

import sys
import heapq

with open("dictall.txt","r") as r:
    fin = r.read().split('\n')

input = open(sys.argv[1],"r").read().strip().split('\n')
writein = open(sys.argv[2],"w")

wordlen = len(input[0].split(',')[0])
biglist = set([i for i in fin if len(i) == wordlen])


bigdict = {}
for word in biglist:
    temp = []
    for x in range(len(word)):
        for y in 'abcdefghijklmnopqrstuvwxyz':
            if y != word[x]:
                xword = word[:x] + y + word[x+1:]
                if xword in biglist:
                    temp.append(xword)
    bigdict[word] = temp


class Node():
    def __init__(self, totalcost, word, pathTo):
        self.word = word
        self.cost = totalcost
        self.path = pathTo

    def comp(self):
        return (self.cost, self.word, self.path)

class WordLadder():
    def __init__(self,start,target):
        self.tempset = set()
        self.fr = []
        self.tempsett = set()
        self.start = start
        self.target = target
        initNode = Node(self.estimate(self.start),self.start,[])
        heapq.heappush(self.fr,initNode.comp())

    def populate(self):
        for word in fin:
            self.tempset.add(word)

    def estimate(self,word):
        diff = 0
        for a in range(len(self.start)):
            if word[a] != self.target[a]:
                diff += 1
        return diff

    def processFrontier(self):
        currentNode = heapq.heappop(self.fr)
        tempWord = currentNode[1]
        self.tempsett.add(tempWord)

        updatePath = list(currentNode[2])
        updatePath.append(tempWord)

        neighbors = bigdict[tempWord]

        for neighbor in neighbors:
            if neighbor not in self.tempsett:
                if neighbor in self.tempset:
                    self.tempset.remove(neighbor)
                newNode = Node(currentNode[0] + self.estimate(neighbor) - self.estimate(tempWord) + 1, neighbor, updatePath)
                heapq.heappush(self.fr,newNode.comp())
        return currentNode

# for pair in input:
#     term = pair.split(',')
#     ladder = WordLadder(term[0], term[1])
#     ladder.populate()
#     while term[1] not in ladder.tempsett:
#         if len(ladder.fr) == 0:
#             finalPath = list(term)
#             break
#         nextWord = ladder.processFrontier()
#         finalPath = list(nextWord[2])
#         finalPath.append(nextWord[1])
#     writein.write(",".join(finalPath))
#     writein.write("\n")

#---------------------------------------------------------------------
#problem 1
#2546
#3,242,331 calculations
# bigfour = []
# for i in biglist:
#     if len(i) == 4:
#         bigfour.append(i)
#
# fourdict = {}
# for word in bigfour:
#     temp = []
#     for x in range(len(word)):
#         for y in 'abcdefghijklmnopqrstuvwxyz':
#             if y != word[x]:
#                 xword = word[:x] + y + word[x+1:]
#                 if xword in bigfour:
#                     temp.append(xword)
#     fourdict[word] = temp
#
# #creates a list of lists of all combinations
# inputfour = []
# i = 0
# j = 1
# while i < len(bigfour):
#     while j < len(bigfour):
#         temp = []
#         temp = [bigfour[i]] + [bigfour[j]]
#         inputfour.append(temp)
#         j += 1
#     i += 1
#     j = i
#
# templen = 0
# for pair in inputfour:
#     ladder = WordLadder(pair[0], pair[1])
#     ladder.populate()
#     while pair[1] not in ladder.tempsett:
#         if len(ladder.fr) == 0:
#             finalPath = list(pair)
#             break
#         nextWord = ladder.processFrontier()
#         finalPath = list(nextWord[2])
#         finalPath.append(nextWord[1])
#     if len(finalPath) > templen:
#         templen = len(finalPath)
#         writein.write(",".join(finalPath))
#         writein.write("\n")
#---------------------------------------------------------------------
#problem 2
# 5119
# 13,104,640 calculations
bigfive = []
for i in biglist:
    if len(i) == 5:
        bigfive.append(i)
fivedict = {}
for word in bigfive:
    temp = []
    for x in range(len(word)):
        for y in 'abcdefghijklmnopqrstuvwxyz':
            if y != word[x]:
                xword = word[:x] + y + word[x+1:]
                if xword in bigfive:
                    temp.append(xword)
    fivedict[word] = temp

inputfive = []
i = 0
j = 1
while i < len(bigfive):
    while j < len(bigfive):
        temp = []
        temp = [bigfive[i]] + [bigfive[j]]
        inputfive.append(temp)
        j += 1
    i += 1
    j = i

templen = 0
for pair in inputfive:
    ladder = WordLadder(pair[0], pair[1])
    ladder.populate()
    while pair[1] not in ladder.tempsett:
        if len(ladder.fr) == 0:
            finalPath = list(pair)
            break
        nextWord = ladder.processFrontier()
        finalPath = list(nextWord[2])
        finalPath.append(nextWord[1])
    if len(finalPath) > templen:
        templen = len(finalPath)
        writein.write(",".join(finalPath))
        writein.write("\n")
# ---------------------------------------------------------------------
# problem 3
# 8301
#34,457,451
# bigsix = []
# for i in biglist:
#     if len(i) == 6:
#         bigsix.append(i)
# sixdict = {}
# for word in bigsix:
#     temp = []
#     for x in range(len(word)):
#         for y in 'abcdefghijklmnopqrstuvwxyz':
#             if y != word[x]:
#                 xword = word[:x] + y + word[x+1:]
#                 if xword in bigsix:
#                     temp.append(xword)
#     sixdict[word] = temp
#
# inputsix = []
# i = 0
# j = 1
# while i < len(bigsix):
#     while j < len(bigsix):
#         temp = []
#         temp = [bigsix[i]] + [bigsix[j]]
#         inputsix.append(temp)
#         j += 1
#     i += 1
#     j = i


# templen = 0
# for pair in inputsix:
#     ladder = WordLadder(pair[0], pair[1])
#     ladder.populate()
#     while pair[1] not in ladder.tempsett:
#         if len(ladder.fr) == 0:
#             finalPath = list(pair)
#             break
#         nextWord = ladder.processFrontier()
#         finalPath = list(nextWord[2])
#         finalPath.append(nextWord[1])
#     if len(finalPath) > templen:
#         templen = len(finalPath)
#         writein.write(",".join(finalPath))
#         writein.write("\n")

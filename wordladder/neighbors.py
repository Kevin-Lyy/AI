#! /usr/bin/python
import sys
with open("dictall.txt","r") as r:
    fin = r.read().split('\n')
input = open(sys.argv[1],"r").read().strip().split('\n')
writein = open(sys.argv[2],"w")

biglist = []
w = len(input[1])
for line in fin:
    if len(line) == len(input[0]):
        biglist.append(line)
bigdict = {}

for word in input:
    dictlist = []
    c = 0
    for werd in biglist:
        diff = 0
        for i in range(len(word)):
            if word[i] != werd[i]:
                diff += 1
        if diff == 1:
            c += 1
            dictlist.append(werd)
            print(dictlist)
    if word == w:
        bigdict[word] = dictlist
    writein.write(str(word) + ',' + str(c) + '\n')

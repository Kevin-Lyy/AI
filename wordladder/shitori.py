#! /usr/bin/python

import sys
import heapq

with open("dictall.txt","r") as r:
    fin = r.read().split('\n')

input = open(sys.argv[1],"r").read().strip().split(',')
writein = open(sys.argv[2],"w")

wordlen = len(input[0].split(',')[0])
biglist = []
for word in fin:
    word.split()
    t = input[0]
    t.split()
    if word:
        if t[-1] == word[0]:
            biglist.append(word)

for word in biglist:
    word.split()
    a = input[1]
    a.split()
    if word[-1] == a[0]:
        writein.write(input[0])
        writein.write(",")
        writein.write(word)
        writein.write(",")
        writein.write(input[1])
        break

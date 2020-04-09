#! /usr/bin/python

#Question 1
import sys
def sortfile():
    f = open(sys.argv[1],"r")
    w = open(sys.argv[2],"w")
    biglist = []
    for line in f:
        line = line.strip()
        line = line.split(",")
        if len(line) > 1 and line[1] != "":
            line = [line[0]] + sorted(line[1:])
            biglist.append(line)
    biglist = sorted(biglist)
    for line in biglist:
        w.write(",".join(line) + "\n")

#Quesion 2
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class Dlist:
    def __init__(self):
        self.head = None

    def insert(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
            temp.next.previous = temp

    def delete(self, value):
        temp = self.head

        while temp:
            if value == temp.value:
                break
            temp = temp.next

        if temp.next == None and temp.value != value:
            return False

        if temp.previous and temp.next:
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            temp.previous = None
            temp.next = None
        elif temp.previous:
            temp.previous.next = None
            temp.previous = None
        elif temp.next:
            self.head = temp.next
            self.head.previous = None
        else:
            self.head = None

        return True

    def tolist(self):
        lst = []
        temp = self.head
        lst.append(temp.value)
        while temp.next != None:
            lst.append(temp.next.value)
            self.delete(temp.next.value)
        lst.sort()
        return lst

#testing

#Test question 1
#sortfile()

#Test question 2
def insert_all(the_dlist, the_input_list):
    for element in the_input_list:
        the_dlist.insert(element)

a = Dlist()
insert_all(a,[4,5,2,3,2,7])
print(a.tolist())

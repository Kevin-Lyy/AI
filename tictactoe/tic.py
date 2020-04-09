# -*- coding: utf-8 -*-
"""Tic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A_XMMl_WmjRr61TYA2IVIT-_48D2qx5u
"""

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = [] # all layouts that can lead to this one, by one move
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('parents:',self.parents)
        print ('children:',self.children)

xwin = set()
owin = set()
draw = set()
inter = set()

#checks for the winner or tie
def winner(layout):

    for i in Wins:
        if layout[i[0]] == 'x' and layout[i[1]] == 'x' and layout[i[2]] == 'x':
            return True, 'x'

        elif layout[i[0]] == 'o' and layout[i[1]] == 'o' and layout[i[2]] == 'o':
            return True, 'o'

    if not('_' in layout):
        return True, 'tie'

    return False, None

def CreateAllBoards(layout,parent):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    #adds the state of the board to allboards if not in it
    if parent and layout not in AllBoards[parent].children:
      AllBoards[parent].children.append(layout)

    state,boardwin = winner(layout)
    board = BoardNode(layout)
    board.parents.append(parent)
    AllBoards[layout] = board

    if state:
      board.endState = boardwin

      if boardwin == 'x':
        xwin.add(layout)
      if boardwin == 'o':
        owin.add(layout)
      if boardwin == 'tie':
        draw.add(layout)

    else:
      inter.add(layout)
      for i in range(0,9):
        blist = list(layout)
        if blist[i] == '_':
          if layout.count('x') == layout.count('o'):
            blist[i] = 'x'
          else:
            blist[i] = 'o'
          blist = ''.join(blist)
          CreateAllBoards(blist,layout)

CreateAllBoards('_________',None)
print('all boards: ', len(AllBoards))

numChildren = 0
for b in AllBoards:
    for c in AllBoards[b].children:
        numChildren += 1

print('children: ', numChildren)
print('x wins: ', len(xwin))
print('o wins: ', len(owin))
print('draws: ', len(draw))
print('intermediate board: ', len(inter))

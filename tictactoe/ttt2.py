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

x_wins = set()
o_wins = set()
draws = set()
intermediates = set()

def WorD(layout):
    #check for win before checking for draw
    for W in Wins:
        if layout[W[0]] == 'x' and layout[W[1]] == 'x' and layout[W[2]] == 'x':
            return True, 'x'
        elif layout[W[0]] == 'o' and layout[W[1]] == 'o' and layout[W[2]] == 'o':
            return True, 'o'
    #board is full
    if not('_' in layout):
        return True, 'd'
    return False, None

def CreateAllBoards(layout,parent):
    #idk why I did this one??
    #if layout in AllBoards:
    if parent and layout not in AllBoards[parent].children:
        AllBoards[parent].children.append(layout)

    terminate,state = WorD(layout)
    if terminate:
        if layout in AllBoards and parent not in AllBoards[layout].parents:
            AllBoards[layout].parents.append(parent)
        else:
            b = BoardNode(layout)
            b.parents.append(parent)
            b.endState = state
            AllBoards[layout] = b

            if state == 'x':
                x_wins.add(layout)
            elif state == 'o':
                o_wins.add(layout)
            elif state == 'd':
                draws.add(layout)

    else:
        if layout in AllBoards and not parent in AllBoards[layout].parents:
            AllBoards[layout].parents.append(parent)
        else:
            b = BoardNode(layout)
            b.parents.append(parent)
            AllBoards[layout] = b
            intermediates.add(layout)
        for index in range(0,9):
            L = list(layout)
            if L[index] == '_':
                if layout.count('x') == layout.count('o'):
                    L[index] = 'x'
                else:
                    L[index] = 'o'
                L = ''.join(L)
                CreateAllBoards(L,layout)

CreateAllBoards('_________',None)
print('all boards: ', len(AllBoards))

numChildren = 0
for b in AllBoards:
    for c in AllBoards[b].children:
        numChildren += 1

print('children: ', numChildren)
print('x_wins: ', len(x_wins))
print('o_wins: ', len(o_wins))
print('draws: ', len(draws))
print('intermediates: ', len(intermediates))

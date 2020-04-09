#! /usr/bin/python3
import random, sys, time

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
        self.children = [] # all layouts that can be reached with a single move
        self.best_move = None # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end = None # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.final_state = None # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('moves to end:',self.moves_to_end)
        print ('final state:',self.final_state)

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

    if layout in AllBoards:
        return
    else:
        AllBoards[layout] = BoardNode(layout)

        tstate,boardwin = winner(layout)

        if tstate:
            AllBoards[layout].endState = boardwin
            AllBoards[layout].best_move = -1
            AllBoards[layout].moves_to_end = 0
            AllBoards[layout].final_state = boardwin
        else:

            if layout.count('x') > layout.count('o'):
                player = 'o'
            else:
                player = 'x'

            for i in range(0,9):
                L = list(layout)
                if L[i] == '_':
                    L[i] = player
                    L = ''.join(L)
                    AllBoards[layout].children.append(L)
                    CreateAllBoards(L,layout)

def bpath(layout,moves):

    if AllBoards[layout].endState:
        return moves,AllBoards[layout].endState
    else:
        movesm = 10
        state = None
        for i in AllBoards[layout].children:
            m,state = bpath(i,moves+1)
            movesm = min(movesm,m)
        return movesm,state

positions = {0: 'top-left',
               1: 'top-middle',
               2: 'top-right',
               3: 'center-left',
               4: 'center-middle',
               5: 'center-right',
               6: 'bottom-left',
               7: 'bottom-middle',
               8: 'bottom-right'}

def nMove(oboard,nboard):
    for i in range(0,9):
        if oboard[i] != nboard[i]:
            return i

def bmove(layout):
    if AllBoards[layout].endState:
        return None
    else:

        if layout.count('x') > layout.count('o'):
            player = 'o'
        else:
            player = 'x'

        fwin = None
        draws = []
        mmoves = None
        newLayout = None
        move = None

        for c in AllBoards[layout].children:

            if AllBoards[c].final_state == player:
                if not fwin or AllBoards[c].moves_to_end < AllBoards[fwin].moves_to_end:
                    fwin = c

            elif AllBoards[c].final_state == 'tie':
                draws.append(c)

            if not mmoves or AllBoards[c].moves_to_end > AllBoards[mmoves].moves_to_end:
                mmoves = c

        if fwin:
            newLayout = fwin
        elif draws:
            print(draws)
            newLayout = random.choice(draws)
        else:
            print(mmoves)
            newLayout = mmoves

        move = nMove(layout,newLayout)

        print('move: '+ str(move))
        print(positions[move])
        print(player + ' wins in ' +
              str(AllBoards[layout].moves_to_end) +
              ' move(s)')
def main():
    START = time.time()

    CreateAllBoards('_________',None)
    for layout in AllBoards:
        if not AllBoards[layout].moves_to_end:
            AllBoards[layout].moves_to_end,AllBoards[layout].final_state = bpath(layout,0)

    bmove(sys.argv[1])

    END = time.time()

    print('time: ' + str(END-START))
main()

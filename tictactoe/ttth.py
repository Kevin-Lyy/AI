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
        ##print ('layout:',self.layout, 'endState:',self.endState)
        ##print ('children:',self.children)
        print ('layout:',self.layout,
               'moves_to_end:', self.moves_to_end,
               'final_state:', self.final_state)

#win or draw
def WorD(layout):
    #check for win before checking for draw
    for W in Wins:
        if layout[W[0]] == 'x' and layout[W[1]] == 'x' and layout[W[2]] == 'x':
            return True, 'x'
        elif layout[W[0]] == 'o' and layout[W[1]] == 'o' and layout[W[2]] == 'o':
            return True, 'o'
    #draw if board is full
    if not('_' in layout):
        return True, 'd'
    return False, None

def CreateAllBoards(layout,parent):
    #if not already recorded in dict of all boards (no need to redo bc wastes time!)
    if layout not in AllBoards:

        #add layout to dict of all boards
        AllBoards[layout] = BoardNode(layout)

        #determines if final board and identity of winner or draw
        terminate,state = WorD(layout)

        if terminate:
            #record winner or draw
            AllBoards[layout].endState = state

            AllBoards[layout].best_move = -1
            AllBoards[layout].moves_to_end = 0
            AllBoards[layout].final_state = state

        else:
            #determine if x or o moves
            player = None
            if layout.count('x') == layout.count('o'):
                player = 'x'
            else:
                player = 'o'

            for index in range(0,9):
                L = list(layout)
                #place letter if empty cell
                if L[index] == '_':
                    L[index] = player
                    L = ''.join(L)
                    #add new board to its children
                    AllBoards[layout].children.append(L)
                    #recurse with new board
                    CreateAllBoards(L,layout)

#determines moves_to_end and final_state
#nmoves = number of moves made so far
def bestPath(layout,nmoves):
    if AllBoards[layout].endState:
        #moves_to_end,final_state
        return nmoves,AllBoards[layout].endState
    else:
        #tree with min num of moves to a win
        #10 since max moves is 9 for a ttt board
        minMoves = 10
        state = None
        for c in AllBoards[layout].children:
            #recurse
            moves,state = bestPath(c,nmoves+1)
            minMoves = min(minMoves,moves)
            #print(c,nmoves+1,minMoves)
        #moves_to_end,final_state
        return minMoves,state

import random

#index: description
descr = {0: 'best move is upper-left',
               1: 'best move is upper-middle',
               2: 'best move is upper-right',
               3: 'best move is center-left',
               4: 'best move is center-middle',
               5: 'best move is center-right',
               6: 'best move is lower-left',
               7: 'best move is lower-middle',
               8: 'best move is lower-right'}

def nextMove(origLayout,nextLayout):
    for index in range(0,9):
        if origLayout[index] != nextLayout[index]:
            return index

def bestMove(layout):
    if AllBoards[layout].endState:
        return None
    else:

        #determine player
        player = None
        if layout.count('x') == layout.count('o'):
            player = 'x'
        else:
            player = 'o'

        fastestWin = None
        draws = []
        mostMoves = None

        newLayout = None
        move = None

        for c in AllBoards[layout].children:
            if AllBoards[c].final_state == player:
                if not fastestWin or AllBoards[c].moves_to_end < AllBoards[fastestWin].moves_to_end:
                    fastestWin = c
            elif AllBoards[c].final_state == 'd':
                draws.append(c)
            if not mostMoves or AllBoards[c].moves_to_end > AllBoards[mostMoves].moves_to_end:
                mostMoves = c

        if fastestWin:
            newLayout = fastestWin
        elif draws:
            print(draws)
            newLayout = random.choice(draws)
        else:
            print(mostMoves)
            newLayout = mostMoves

        move = nextMove(layout,newLayout)

        print('move=',move)
        print(descr[move])
        print(player,
              'wins in ',
              AllBoards[layout].moves_to_end,
              ' move(s)')

def main():
    import sys
    import time

    START = time.time()

    CreateAllBoards('_________',None)
    #sets moves_to_end and final_state
    for layout in AllBoards:
        if not AllBoards[layout].moves_to_end:
            AllBoards[layout].moves_to_end,AllBoards[layout].final_state = bestPath(layout,0)

    bestMove(sys.argv[1])

    END = time.time()

    #should be under 2 seconds
    print('time:', END-START)
main()

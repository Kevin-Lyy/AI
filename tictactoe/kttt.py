#! /usr/bin/python3
import random, sys

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# Best future states according to the player viewing this board
ST_X = 1  # X wins
ST_O = 2  # O wins
ST_D = 3  # Draw

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {}   # This is primarily for debugging: key = layout, value = BoardNode

class BoardNode:

    def __init__(self, layout):
        self.layout = layout
        self.mover = 'x' if layout.count('x') == layout.count('o') else 'o'

        self.state = BoardNode.this_state(self, layout) # if final board, then ST_X, ST_O or ST_D, else None
        if self.state is None:
            self.best_final_state = None           # best achievable future state: ST_X, ST_O or ST_D
            self.best_move = None                  # 0-9 to achieve best state
            self.num_moves_to_final_state = None   # number of moves to best state
        else:
            self.best_final_state = self.state
            self.best_move = -1
            self.num_moves_to_final_state = 0

        self.children = set()

    def print_me(self):
        print('layout:',self.layout)
        print('mover:',self.mover)
        print('state:',BoardNode.str_state(self, self.state))
        print('best_final_state:',BoardNode.str_state(self, self.best_final_state))
        print('best_move:',self.best_move,BoardNode.str_move(self, self.best_move))
        print('num_moves_to_final_state:',self.num_moves_to_final_state)

    def print_layout(self):
        print('%s\n%s\n%s' % (' '.join(self.layout[0:3]),' '.join(self.layout[3:6]),' '.join(self.layout[6:9])))

    # =================== class methods  =======================
    def str_state(self, state):
        # human description of a state
        return 'None' if state is None else ['x-wins','o-wins','draw'][state-1]

    def str_move(self, move):
        # human description of a move
        moves = ('top-left','top-center','top-right',\
                 'middle-left','middle-center','middle-right',\
                 'bottom-left','bottom-center','bottom-right')
        return 'done' if move == -1 else moves[move]

    def this_state(self, layout):
        # classifies this layout as None if not final, otherwise ST_X or ST_O or ST_D
        for awin in Wins:
            if layout[awin[0]] != '_' and layout[awin[0]] == layout[awin[1]] == layout[awin[2]]:
                return ST_X if layout[awin[0]] == 'x' else ST_O
        if layout.count('_') == 0:
            return ST_D
        return None

def CreateAllBoards(layout):
    # Populate AllBoards with finally calculated BoardNodes

    if layout in AllBoards:
        return

    anode = BoardNode(layout)
    # if this is an end board, then all of its properties have already be calculated by __init__()
    if anode.state is not None:
        AllBoards[layout] = anode
        return

    # expand children if this is not a final state
    move = 'x' if layout.count('x') == layout.count('o') else 'o'
    for pos in range(9):
        if layout[pos] == '_':
            new_layout = layout[:pos] + move + layout[pos+1:]
            if new_layout not in AllBoards:
                CreateAllBoards(new_layout)
            anode.children.add(new_layout)

    bestMoveList = list()
    winList = list()
    drawList = list()
    loseList = list()
    for child in anode.children:
        if move == "x" and AllBoards[child].best_final_state == ST_X:
            winList += [AllBoards[child]]
        elif move == "o" and AllBoards[child].best_final_state == ST_O:
            winList += [AllBoards[child]]
        elif AllBoards[child].best_final_state == ST_D:
            drawList += [AllBoards[child]]
        else:
            loseList += [AllBoards[child]]

    if len(winList) != 0:
        winList.sort(key=lambda x: x.num_moves_to_final_state)
        anode.num_moves_to_final_state = winList[0].num_moves_to_final_state + 1
        if move == "x":
            anode.best_final_state = ST_X
        else:
            anode.best_final_state = ST_O
        bestMoveList = [x.layout for x in winList if x.num_moves_to_final_state == winList[0].num_moves_to_final_state]
    elif len(drawList) != 0:
        drawList.sort(key=lambda x: x.num_moves_to_final_state, reverse = True)
        anode.num_moves_to_final_state = drawList[0].num_moves_to_final_state + 1
        anode.best_final_state = ST_D
        bestMoveList = [x.layout for x in drawList if x.num_moves_to_final_state == drawList[0].num_moves_to_final_state]
    elif len(loseList) != 0:
        loseList.sort(key=lambda x: x.num_moves_to_final_state, reverse = True)
        anode.num_moves_to_final_state = loseList[0].num_moves_to_final_state + 1
        if move == "o":
            anode.best_final_state = ST_X
        else:
            anode.best_final_state = ST_O
        bestMoveList = [x.layout for x in loseList if x.num_moves_to_final_state == loseList[0].num_moves_to_final_state]

    if len(anode.children) != 0:
        bestMove = random.choice(bestMoveList)
        for i in range(9):
            if bestMove[i] != anode.layout[i]:
                anode.best_move = i
                break

    AllBoards[layout] = anode

# Random move TicTacToe competitor
Usage = '''
TTT-Random.py board={9-char} result_prefix={prefix} result_file={filename}
       will write a move to filename (if result_file is provided)
       else print move
   or
TTT-Random.py id=1 result_prefix=(prefix) result_file={filename}
       will write AUTHOR and TITLE to filename (if result_file is provided)
       else print them
'''

AUTHOR = 'Kenny Li'
TITLE = 'TTT Competitor'


def main():
    if len(sys.argv) < 2:
        print (Usage)
        return
    dct = getargs()
    result = ''
    if 'id' in dct:
        result='author=%s\ntitle=%s\n' % (AUTHOR,TITLE)
    elif 'board' in dct:
        board=dct['board']
        if len(board) != 9:
            result='Error: board must be 9 characters'
        else:
            if (AllBoards[board].best_move != -1):
                result='move=' + str(AllBoards[board].best_move) + '\nBest move: ' + AllBoards[board].str_move(AllBoards[board].best_move) + ". " + AllBoards[board].str_state(AllBoards[board].best_final_state) + " in " + str(AllBoards[board].num_moves_to_final_state - 1) + " moves."
            else:
                result='Game is over!'
    if 'result_prefix' in dct:
        result = dct['result_prefix']+'\n'+result
    if 'result_file' in dct:
        try:
            f=open(dct['result_file'],'w')
            f.write(result)
            f.close()
        except:
            print ('Cannot open: %s\n%s\n' % (dct['result_file'],result))
    else:
        print (result)

def getargs():
    dct = {}
    for i in range(1,len(sys.argv)):
        sides = sys.argv[i].split('=')
        if len(sides) == 2:
            dct[sides[0]] = sides[1]
    return dct

CreateAllBoards("_________")
main()

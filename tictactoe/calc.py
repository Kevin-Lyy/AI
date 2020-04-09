import sys

board = []

def checkboard(board):
    if (board[0] == board[1] and board[1] == board[2]):
        return False
    if (board[0] == board[3] and board[3] == board[6]):
        return False
    if (board[0] == board[4] and board[4] == board[8]):
        return False
    if (board[1] == board[4] and board[4] == board[7]):
        return False
    if (board[2] == board[4] and board[4] == board[6]):
        return False
    if (board[2] == board[5] and board[5] == board[8]):
        return False
    if (board[3] == board[4] and board[4] == board[5]):
        return False
    if (board[6] == board[7] and board[7] == board[8]):
        return False
    return True
# 255168
# 131184
# 77904
# 46080
# 5478
# 765

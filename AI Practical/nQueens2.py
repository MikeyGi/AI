N = int(input("Enter the number of queens"))
queen = 'Q'
empty = '-'
board = [[empty]* N for i in range(N)]

def isSafe(i, j):
    for k in range(N):
        if board[i][k] == queen or board[k][j] == queen:
            return False
        
    for m in range(N):
        for n in range(N):
            if i+j == m+n or i-j == m-n:
                if board[m][n] == queen:
                    return False
    return True

def nqueen(noq):
    if(noq==0):
        return True
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != queen and isSafe(i,j):
                board[i][j] = queen
                if nqueen(noq -1) == True:
                    return True
                board[i][j] = empty

    return False

def printBoard(board):
    for i in board:
        print(i)

if nqueen(N):
    printBoard(board)
else:
    print("can't place")

''''
Time complexity of Nqueen Problem is : O(N!) .
'''
def nqueen(board , n, r ):
    if r >= n :
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1 :
                    print("Q",end="  ")
                else :
                    print("X", end="  ")
            print()
        print()
        print()
        return
    else :
        for c in range(0 , n):

             if isSafe(board , n , r , c ):

                board[r][c] = 1

                nqueen(board , n , r+1 )

                board[r][c] = 0

        return

def isSafe(board , n , r, c):

    for i in range(0,r):
        if board[i][c]==1:
            return False

    leftR = r-1
    leftC= c-1
    while leftR >= 0 and leftC >= 0 :
        if board[leftR][leftC]==1:
            return  False
        leftR -= 1
        leftC -= 1

    rightR = r-1
    rightC = c+1

    while rightR >= 0 and rightC <= n-1:

        if board[rightR][rightC] == 1:
            return False
        rightR -= 1
        rightC += 1

    return True

n = 4
board = [[0 for _ in range(n)] for _ in range(n)]
nqueen(board , n , 0 )



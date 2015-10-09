file = open('attack.txt')
board = []
for line in file:
    board.append(line.strip().split('/'))
origboard = board
for i in range(len(board)):
    board[i][7] = board[i][7].replace(" w - - 0 1","") ##removes thingy at end
#is already ordered in rows via FEN
#must check for column and diagonal uniquenesss
for k in range(len(board)): ##changes FEN to column positions
    for j in range(len(board[k])):
        if len(board[k][j]) == 3:
            board[k][j] = (int(board[k][j][0])+1) 
        elif len(board[k][j]) < 3:
            if board[k][j][0] == "Q":
                 board[k][j] = (8-int(board[k][j][1]))
            else:
                 board[k][j] = (int(board[k][j][0])+1)

badboard = []
#checks for column uniqueness and removes if not unique
count = 0
for o in range(len(board)):
    for n in range(len(board[o])): 
        for m in range(n+1,(len(board[o])),1):
            if board[o][n] != board[o][m]:
                count+= 1
#if there is a duplicate or is out of range, increments count
if count != 28:
    badboard.append(board[o]) #if there is a duplicate of range error, moved to bad board
    board.remove(board[o]) #if columns and ranges are good, remains in 'board' list

for a in range(len(board)):
    board[a].append("Eight Queens!")
print(board)
x = open('attack.sol','a')
x.write(str(board))
x.write(str(badboard))
x.close()
            
        

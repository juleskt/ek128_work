file = open("sudokuboard.txt")

board = []
for line in file:
    board.append(line.strip())

count = 0

def solverow(x,y):
    for i in range(0,len(x)):
        for j in range(1,10):
            if str(j) in x[i]:
                y+= 1
    if y == 81:
        print("Valid")
    else:
        print("Invalid")
    

solverow(board,count)

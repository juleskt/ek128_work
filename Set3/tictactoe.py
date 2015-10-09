file = open('tictactoeboards.txt')
board = []
for line in file:
    board.append(line.strip())

length = len(board[0])
length = int (length)

valid = []
invalid = []
won = []
xwin = []
ywin = []
incomplete = []
what = []

def validity(x):
    for a in range(0,len(x),1):
        c1 = 0
        c2 = 0
        for let in x[a]:
            
            if let == "x":
                c1+= 1
                
            if let == "o":
                c2+=1
                
        if c1 >= c2 and abs(c1-c2) < 2:
            valid.append(board[a])
        else:
            invalid.append(board[a])
            
def wins_and_ties(x,y):
    #CHECKING FOR WINS/Completion
    ##print(len(x))
    for i in range(len(x)): ##rows broo
        for j in range(2,y,3):
            if (x[i][j] == x[i][j-1])and(x[i][j] == x[i][j-2]):
                won.append(x[i])
        for l in range(0,2,1): ##columns yeaaaah
            if (x[i][l] == x[i][l+3])and(x[i][j] == x[i][l+3]):
                won.append(x[i])
        if x[i][0] == x[i][4] and x[i][0] == x[i][8]: ##diag broo
            won.append(x[i])
        if x[i][2] == x[i][4] and x[i][2] == x[i][6]: ##diag broo
            won.append(x[i])
        #for "x" not in x[i]:
##    print((won))
            

def differentiatedwins(x,y,xwin,ywin):
    #Checks who won
    for i in range(len(x)): ##rows broo
        for j in range(2,y,3):
            if (x[i][j] == x[i][j-1])and(x[i][j] == x[i][j-2]):
                if x[i][j] == 'x':
                    xwin.append(x[i])
                elif x[i][j] == 'o':
                    ywin.append(x[i])
                elif x[i][j] == '#':
                    incomplete.append(x[i])
        for l in range(0,2,1): ##columns yeaaaah
            if (x[i][l] == x[i][l+3])and(x[i][j] == x[i][l+3]):
                if x[i][j] == 'x':
                    xwin.append(x[i])
                elif x[i][j] == 'o':
                    ywin.append(x[i])
                elif x[i][j] == '#':
                    incomplete.append(x[i])
        if x[i][0] == x[i][4] and x[i][0] == x[i][8]: ##diag broo
                if x[i][j] == 'x':
                    xwin.append(x[i])
                elif x[i][j] == 'o':
                    ywin.append(x[i])
                elif x[i][j] == '#':
                    incomplete.append(x[i])
        if x[i][2] == x[i][4] and x[i][2] == x[i][6]: ##diag broo
                if x[i][j] == 'x':
                    xwin.append(x[i])
                elif x[i][j] == 'o':
                    ywin.append(x[i])
                elif x[i][j] == '#':
                    incomplete.append(x[i])
     
validity(board)
wins_and_ties(valid,length)
differentiatedwins(won,length,xwin,ywin)
for a in range(len(xwin)):
    xwin.append(' x')
for b in range(len(ywin)):
    ywin.append(' y')
for c in range(len(incomplete)):
    incomplete.append(' inc')
for d in range(len(invalid)):
    invalid.append(' i')

x = open('tttstatus','a')
x.write(str(xwin))
x.write(str(ywin))
x.write(str(incomplete))
x.write(str(invalid))
x.close()

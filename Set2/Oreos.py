file = open('coded_msg.txt')
oreolist = []
for line in file:
    oreolist.append(line.strip())

filed = open('words.txt')
wordlist = []
for line in filed:
    wordlist.append(line.strip())

track = 0 

def makewords(x,y,z):
    word = ''
    for j in range (1,len(y)+1,1):
        if j % 2 != 0:
            word = y[j-1][0]+y[j]+y[j-1][1]
            if word not in z:
                print(word)

makewords(track,oreolist,wordlist)

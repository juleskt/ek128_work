a = input("How many rows would you like your pyramid?")

a = int (a)

alpha = 'abcdefghijklmnopqrstuvwxyz'

num = 1

d = "-"
ognum = 0

for i in range(0,a,1):
    ogdiv = ognum/26
    ogdiv = int (ogdiv)
    numdiv = num/26
    numdiv = int (numdiv)
    printtimes = (numdiv - ogdiv)-1

    if ogdiv == numdiv:
        print((a-i)*d,alpha[ognum%26:num%26],(a-i)*d)

    elif ogdiv != numdiv:
        print((a-i)*d,alpha[ognum%26:26]+alpha*printtimes+alpha[0:num%26],(a-i)*d)

    ognum = num
    num = num+3+(i*2)

a = input("What is the lower bound of the range that you'd like to test?")
b = input("What is the upper bound of the range that you'd like to test?")
c = input("Would you like a multiple in there, too? (Enter 0 if none)")
d = input("A first digit? (Enter 0 if none)")
a = int (a)
b = int (b)
c = int (c)

test = a%2
def even_minus_odd(start,end,multiple,first_digit):
    x = 0
    y = 0

    if test == 0:
        if multiple == 0:
            if first_digit == 0:
                for i in range(start,end+1,2): 
                    x+=i
                
                for j in range(start+1,end+1,2): 
                    y+=j

            if first_digit !=0:
                for i in range(start,end+1,2): 
                    if str(i)[0] == first_digit:
                        x+=i

                for j in range(start+1,end+1,2): 
                    if str(j)[0] == first_digit:
                        y+=j

        if multiple != 0:
            if first_digit == 0:
                for m in range(start,end+1,2):
                    if m%multiple == 0:
                         x+=m

                for n in range(start+1,end+1,2): 
                    if n%multiple == 0:
                        y+=n

            if first_digit != 0:
                for m in range(start,end+1,2):
                    if m%multiple == 0:
                        if str(m)[0] == first_digit:
                            x+=m

                for n in range(start+1,end+1,2): 
                    if n%multiple == 0:
                        if str(n)[0] == first_digit:
                            y+= n
        print(x-y)



    if test != 0:
        if multiple == 0:
            if first_digit == 0:
                for k in range(start,end+1,2):
                    x+=k
                
                for l in range(start+1,end+1,2):
                    y+=l

            if first_digit != 0:
                for k in range(start,end+1,2):
                    if str(k)[0] == first_digit:
                        x+=k
                
                for l in range(start+1,end+1,2):
                    if str(l)[0] == first_digit:
                        y+=l


        if multiple != 0:
            if first_digit == 0:
                for o in range(start,end+1,2):
                    if o%multiple == 0:
                        x+=o
                            
                for p in range(start+1,end+1,2): 
                    if p%multiple == 0:
                        y+= p
                            
            if first_digit !=0:
                for o in range(start,end+1,2):
                    if o%multiple == 0:
                        if str(o)[0] == first_digit:
                            x+=o
                     
                for p in range(start+1,end+1,2): 
                    if p%multiple == 0:
                        if str(p)[0] == first_digit:
                            y+= p
        print(y-x)
 
even_minus_odd(a,b,c,d)

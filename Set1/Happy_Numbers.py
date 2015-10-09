n = input("Tell me your number, I'll let you know if its happy or clinically depressed")
a = n
z = 0

def ishappy(n,z):
    count = 0
    while(True):
        z = 0
        for x in str(n):
            z += int(x)**2

        n = z
        count = count+1

        if z == 1:
            print("True",count)
            return True
            break
        elif z == 4:
            print("False")
            return False
            break

ishappy(n,z)

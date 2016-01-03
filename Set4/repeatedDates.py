import datetime
from datetime import timedelta
import time

file = open('datelist.txt')
datelist = [] #list of all input dates
newdates = [] #converted list of dates
weekdaycheck = [] #list of A B d Y style dates
intervallist = [] #list of dates within the interval 11/20/1997 - 11/12/2027
for line in file:
    datelist.extend(line.strip().split(';'))

##if datelist[0] == 'Monday September 07, 2015':
##    print("Yes")
##else:
##    print("Wut")
def datesolver(datelist):
    for line in datelist:
        OK = False
        try:
            tt = time.strptime(line,"%A %B %d, %Y")##(Weekdyname,mnthname, day, Year)
            y = datetime.date(tt[0], tt[1], tt[2])
            newdates.append(y)
            weekdaycheck.append(line)
            OK = True
                    except:
            None
        try:
            tt = time.strptime(line,"%Y-%m-%d") ##(Year, month, day)
            z = datetime.date(tt[0], tt[1], tt[2])
            newdates.append(z)
            OK = True
        except:
            None
        try:
            tt = time.strptime(line,"%m/%d/%Y")##(month,day,year)
            x = datetime.date(tt[0], tt[1], tt[2])
            newdates.append(x)
            OK = True
        except:
            None
        try:
            tt = time.strptime(line,"%b %d %Y")##(abbrev month, day, Year)
            w = datetime.date(tt[0], tt[1], tt[2])
            newdates.append(w)
            OK = True
        except:
            None
            
        if line and not OK:
            print(line,"is an invalid date.")

datesolver(datelist)
sortedstuff = sorted(newdates)

for line in sortedstuff:
    if line < datetime.date(2027, 11, 13) and  line > datetime.date(1997, 11, 19):
        intervallist.append(line)
    else:
        None
start = datetime.date(1997, 11, 20)
for line in intervallist:
    if line != start:
        print(start, "is missing from the interval!")
        break
    else:
        start = start + timedelta(1)


for line in weekdaycheck:
    tt = time.strptime(line,"%A %B %d, %Y")
    d = datetime.date(tt[0],tt[1],tt[2])
    if line[:3] != d.strftime("%a"):
        print(line,"has the wrong day of the week! Its actually",d.strftime("%A"),".")
    else:
        None

repeateddates = set()
for date in newdates:
    if newdates.count(date) > 1:
        repeateddates.add(date)
print(sorted(repeateddates)[0],"is the first repeated date.")
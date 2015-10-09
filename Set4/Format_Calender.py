import datetime
from datetime import timedelta
start = datetime.date(2014,1,1)
count = 0
for i in range(1,365,1):
    newdate = start + timedelta(1)
    start = newdate
    thing = newdate.ctime()
    thing = thing[:-14]
    print(thing)


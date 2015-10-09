
file = open('workrecord.txt')
record = []
for line in file:
    record.append(line.strip().split())

idfile = open('employeerecord.csv')
eid = []
for line in idfile:
    eid.append(line.strip().split(','))

earned = 0

for i in range(0,len(eid),1):
    for j in range(0,len(record),1):
        if eid[i][2] == record[j][0]:
            earned += float(eid[i][3])*float(record[j][1])
print("Total earned by all employees: $",earned)


#Clinton last name
CEarned = 0
for k in range(0,len(eid),1):
    for l in range(0,len(record),1):
        if eid[k][1] == 'Clinton':
            if eid[k][2] == record[l][0]:
                CEarned += float(eid[k][3])*float(record[l][1])
print("Total that Clintons earned: $",CEarned)

#Barack first name
BEarned = 0
for k in range(0,len(eid),1):
    for l in range(0,len(record),1):
        if eid[k][0] == 'Barack':
            if eid[k][2] == record[l][0]:
                BEarned += float(eid[k][3])*float(record[l][1])
print("Total that Baracks earned: $",BEarned)
##The format for workrecord is
##ID,hours-worked 
##The format for employeerecord.csv is
##First,Last,ID,hourlyrate




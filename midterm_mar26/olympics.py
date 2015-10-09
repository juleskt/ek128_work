# Write the function give_medals
#

"""The dictionary Results contains the names of contestands as keys,
and their times in a swimming event as values. Smaller times are better.
Return a dictionary with the same keys as *Results* but with the values being
 
 "Gold" for the 1st place finisher
 "Silver" for the 2nd place finisher
 "Bronze" for the 3th place finisher
 "4th" for the 4th place finisher
 "5th" for 5th place
 "" for everyone else (empty string)
 
 Bonus/Extra credit: handle ties so that if there is a tie, the next position is vacant:

 Example: if there is a tie for first, and a tie for "fourth", the results will be
 Gold
 Gold
 Bronze
 4th
 4th


 """
D={'a':5,'b':3,'c':2.1,'d':6}
def give_medals(Results):
    SortedResults = sorted(Results.values())
    for i in range (len(SortedResults)):
        if i == 0:
            SortedResults[i] = 'Gold'
        if i == 1:
            SortedResults[i] = 'Silver'
        if i == 2:
            SortedResults[i] = 'Bronze'
        if i == 3:
            SortedResults[i] = '4th'
        if i == 4:
            SortedResults[i] = '5th'
        if i > 4:
            SortedResults[i] = ""
    print(SortedResults)
    return (SortedResults)
    
    



##if __name__=="__main__":
##    D={'a':5,'b':3,'c':2.1}
##    assert give_medals(D)=={'a':'Bronze','b':'Silver','c':'Gold'}
give_medals(D)
    

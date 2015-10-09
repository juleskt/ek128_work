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
def give_medals(Results):
    pass # replace pass with your code



if __name__=="__main__":
    D={'a':5,'b':3,'c':2.1}
    assert give_medals(D)=={'a':'Bronze','b':'Silver','c':'Gold'}
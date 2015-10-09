# Write the function commonsuffix

"""A function that calculates which words have the same suffix."""

def commonsuffix(WordList,suffix):
    """return a list of words in WordList with the ending *suffix*"""
    pass # replace pass with your code


# Note: the assert statements will give errors until the function
# is correctly written.

if __name__=="__main__":
    L=['test','sit','candy','mist']
    Lc=L[:]
    assert commonsuffix(L,'t')==['test','sit','mist']
    assert commonsuffix(L,'st')==['test','mist']
    assert commonsuffix(L,'ic')==None
    assert Lc==L # dont change L
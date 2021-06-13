"""
Problem:

    
A popular gameshow has a words round where contestants are required to guess at
    
a word when it is written without any vowels in it.  For example, a clue might
    
be "bldng" and the answer would be "building".

    
The function 'clue' should take a word, and print out the corresponding clue
    
for that word - the word minus any vowels.


Tests:

    
>>> clue("building")
   
bldng
    
>>> clue("atmosphere")
    
tmsphr
    
>>> clue("perpendicular")
    
prpndclr
    
>>> clue("recipe")
    
rcp
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def clue(word):
    print(''.join([char for char in word if char not in "aeiou"]))

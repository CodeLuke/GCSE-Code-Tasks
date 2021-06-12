"""
Problem:

    
A desperate gambler has bet all of his money on a final last throw of the die.
    
If he rolls a six, he survives to fight another day.
    
Anything else, and he gets thrown to the thugs waiting for him in the back alley.

    
The gone_bust function takes an integer n, and should print either "Pheww!" or
    
"HELP! HELP!" depending on whether he survives or not.
Tests:

>>> gone_bust(2)
HELP! HELP!
    
>>> gone_bust(6)    
Pheww!

>>> gone_bust(10) 
HELP! HELP!
"""
# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def gone_bust(roll):
    if roll == 6:
        print("Pheww!")
    else:
        print("HELP! HELP!")

if __name__ == "__main__":
    run_tests()
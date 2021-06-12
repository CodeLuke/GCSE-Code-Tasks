"""
Problem:

     
A game is played by trying to score exactly 100 points.
     
The function hit_100 takes in a number of points. If the score is
     
100, it should print "Winner!". For scores over 100, it should
     
print "Too high", and for scores under 100 it should print "Too low"

Tests:

    
>>> hit_100(72)
Too low
    
>>> hit_100(135)
Too high
    
>>> hit_100(100)    
Winner!
"""

import doctest
def run_tests():
    doctest.testmod(verbose=True)

def hit_100(num):
    # Simple version
    if num == 100:
        print("Winner!")
    elif num < 100:
        print("Too low")
    else:
        print("Too high")

    """Single line version
    print("Winner!" if num == 100 else "Too low" if num < 100 else "Too high")
    """

if __name__ == "__main__":
    run_tests()
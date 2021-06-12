"""
Problem:

    
A game involves rolling two dice and adding the scores together to
    
calculate the number of points received. However, if a player rolls
    
two dice with the same number, they receive double the points.

    
The roll_double function takes in two numbers, one for each score
    
on the dice. It should print out how many points the player should
    
receive.

Tests:

    
>>> roll_double(2, 5)
7
    
>>> roll_double(4, 5)
9
    
>>> roll_double(2, 2)
8
    
>>> roll_double(5, 5)
20
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def roll_double(x, y):
    # Simple version
    total = x + y
    if x == y:
        print(total * 2)
    else:
        print(total)
    """One line version
    print((x+y)*2 if x == y else x + y)
    """
if __name__ == "__main__":
    run_tests()
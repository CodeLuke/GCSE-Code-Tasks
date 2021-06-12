"""
Problem:

    
The function biggest takes in three variables: a, b and c.
    
It should print out the biggest of the three.

Tests:

    
>>> biggest(10, 12, 7)
12
    
>>> biggest(27, 16, 22)
27
    
>>> biggest(15, 11, 19)    
19
    
>>> biggest(11, 6, 11)    
11
"""
# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)


def biggest(x, y, z):
    """
    This problem has numerous solutions ranging from naive (using a series of if statements which is not scalable) to simple (using the max() function).
    If you are new, don't worry about what your solution is as long as it works, although I would discourage use of the max() function as it doesn't help your learning.
    My solution will sit somewhere in the middle, it will be scalable but still only use simple structures
    """
    biggest = None
    for num in [x, y, z]:
        if biggest is None:
            biggest = num
        elif biggest < num:
            biggest = num
    
    print(biggest)


if __name__ == "__main__":
    run_tests()
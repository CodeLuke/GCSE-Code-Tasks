"""
Problem:

    
Given a list of integers, nums, and another integer, n,
    
the function 'multiply' should print out a new list
    
with each item in the original list multipled by n.

Tests:

    
>>> multiply([1, 2, 3, 4], 2)
[2, 4, 6, 8]
    
>>> multiply([3, 7, 9], 3)
[9, 21, 27]
    
>>> multiply([2, -4, 5], -5)
[-10, 20, -25]
    
>>> multiply([1, 10, 100], 0)
[0, 0, 0]
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def multiply(nums, n):
    print([num * n for num in nums])

if __name__ == "__main__":
    run_tests()
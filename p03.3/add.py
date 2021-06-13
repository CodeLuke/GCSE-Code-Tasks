"""
Problem:

    
The function 'add' takes a list of integers, nums.
    
It should add them all up and print the total.

Tests:

    
>>> add([1, 2, 3])
6
    
>>> add([5, 7, 9])
21
    
>>> add([2, 3, -6])
-1
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def add(nums):
    print(sum(nums))

if __name__ == "__main__":
    run_tests()
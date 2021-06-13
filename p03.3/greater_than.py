"""
Problem:

    
The function 'greater' takes a list of integers, nums, and another
    
integer, n.  It should count the number of items in the list that
    
are greater than n and print this.

Tests:

    
>>> greater([1, 2, 3, 4], 2)
2
    
>>> greater([5, 3, 2, 7], 4)
2
    
>>> greater([3, 7, 4, 9, 10], 1)
5
    
>>> greater([1, 2, 3], 6)
0
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def greater(nums, n):
    print(sum([1 for num in nums if num > n]))

if __name__ == "__main__":
    run_tests()
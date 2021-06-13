"""
Problem:

    
Given a list of integers, nums, and two integers, a and b, we would like
    
to find out which one occurs most frequently in our list.
    
If either a or b appears more often, print that number.
    
If neither appears at all, print "Neither".
    
If they appear the same number of times, print "Tie".
    


Tests:

    
>>> mode([1, 2, 3, 3], 2, 3)
3
    
>>> mode([1, 2, 2, 3, 4], 2, 3)
2
    
>>> mode([1, 2, 2, 1, 2], 3, 4)
Neither
    
>>> mode([2, 2, 3, 3], 2, 3)
Tie
    
>>> mode([], 1, 2)
Neither
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def mode(nums, a, b):
    a_count = nums.count(a)
    b_count = nums.count(b)
    if a_count > b_count:
        print(a)
    elif a_count < b_count:
        print(b)
    elif a_count == 0 and b_count == 0:
        print("Neither")
    else:
        print("Tie")

if __name__ == "__main__":
    run_tests()
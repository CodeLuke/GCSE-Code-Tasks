"""
Problem:

    
Given a list of integers, nums, find out whether the first item
    
in the list is repeated again later.
    
If it is, print "Repeated", otherwise print "Unique".
    
The list will always have a length of at least 1.


Tests:

    
>>> is_repeated([1, 2, 3, 1])
Repeated
    
>>> is_repeated([2, 4, 4, 2, 1, 5])
Repeated
    
>>> is_repeated([5, 4, 3, 2, 1])
Unique
    
>>> is_repeated([8, 6, 2])
Unique
    
>>> is_repeated([5])
Unique
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)


def is_repeated(nums):
    if nums.count(nums[0]) > 1:
        print("Repeated")
    else:
        print("Unique")

if __name__ == "__main__":
    run_tests()
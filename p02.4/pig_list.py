"""
Problem:

    
Given a list of integers, nums, the function `rotate` should move
    
the first item in the list to the end, and then print it.
    
If the list is empty, it should just print the empty list.

Tests:

    
>>> rotate([1, 2, 3, 4])
[2, 3, 4, 1]
    
>>> rotate([5, 7, 9, 2, 1, 4])
[7, 9, 2, 1, 4, 5]
    
>>> rotate([2])
[2]
    
>>> rotate([])  
[]

"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def rotate(nums):
    if len(nums) > 0:
        print(nums[1:] + [nums[0]])
    else:
        print([])
if __name__ == "__main__":
    run_tests()
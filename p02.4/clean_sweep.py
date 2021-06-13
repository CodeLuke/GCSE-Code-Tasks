"""
Problem:

    
Given a list of integers, nums, and an integer, n, the function `clean`
    
should remove all occurences of n in the list.
    
It should then print the list.

    
Warning: You will get an error if you try to remove an item that doesn't
    
exist in the list. Ensure the item is in the list before you try to remove it.



Tests:

    
>>> clean([1, 2, 3, 4], 3)
[1, 2, 4]
    
>>> clean([1, 2, 2, 3, 4], 2)
[1, 3, 4]
    
>>> clean([1, 2, 3, 4, 5], 8)
[1, 2, 3, 4, 5]
    
>>> clean([5, 5, 5, 5, 5, 5, 5], 5)
[]
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def clean(nums, n):
    for _ in range(nums.count(n)):
        nums.remove(n)
    
    print(nums)

if __name__ == "__main__":
    run_tests()
"""
Problem:

    
The function 'cons' takes a list of integers, nums.
    
If any two consecutive items in the list are the same, it
    
should print "Match", otherwise it should print "No match"

Tests:

    
>>> cons([1, 1])
Match
    
>>> cons([1, 2, 3, 4, 4, 5])
Match
    
>>> cons([3, 4, 3, 4, 3])
No match
    
>>> cons([])
No match
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def cons(nums):
    found_cons = False
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            found_cons = True
    print("Match" if found_cons else "No match")

if __name__ == "__main__":
    run_tests()
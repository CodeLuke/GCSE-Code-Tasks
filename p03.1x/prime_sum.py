"""
Problem:

    
The function add_primes takes an integer, n, and should add all 
    
the prime numbers less than or equal to n.

    
e.g. add_primes(13) = 2 + 3 + 5 + 7 + 11 + 13 = 

Tests:

    
>>> add_primes(13)
41
    
>>> add_primes(30)
129
    
>>> add_primes(1500)
165040


Hint:
Could use your is_prime function here from the previous problem?
"""
import doctest
import math
def run_tests():
    doctest.testmod(verbose=True)

def add_primes(n):
    # Numbers from 2 to n (inclusive)
    nums = [x for x in range(2, n + 1)]
    factor = 0
    # Only have to check up to sqrt
    while factor < math.sqrt(n):
        # Remove all multiples of the factor from the list
        for i in nums[factor + 1:]:
            if i % nums[factor] == 0:
               nums.remove(i)
        factor += 1 
    return sum(nums)

if __name__ == "__main__":
    run_tests()
"""
Problem:

    
The function is_prime takes in an intger and tests
    
whether it is prime or not. It should print either
    
"Prime" or "Non-Prime".

Tests:

    
>>> is_prime(1)
Non-Prime
    
>>> is_prime(2)
Prime
    
>>> is_prime(7)
Prime
    
>>> is_prime(24)
Non-Prime
    
>>> is_prime(123)
Non-Prime
    
>>> is_prime(137)
Prime

Hint: 
Count the number of factors!
"""
import doctest
import math
def run_tests():
    doctest.testmod(verbose=True)


def is_prime(n):
    is_prime = True
    if n == 1:
        is_prime = False
    else:    
        for i in range(3, math.floor(math.sqrt(n)), 2):
            if n % i == 0:
                is_prime = False
                break
    
    print("Prime" if is_prime else "Non-Prime")

if __name__ == "__main__":
    run_tests()

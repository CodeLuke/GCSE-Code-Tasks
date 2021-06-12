"""
Problem:

    
The function factor_test takes in two numbers, a and b.
    
If a and b are the same - print "a = b"
    
If a is a factor of b - print "a is a factor of b"
    
If b is a factor of a - print "b is a factor of a"
    
Otherwise, print "No factors here"

Tests:

    
>>> factor_test(10, 5)
b is a factor of a
    
>>> factor_test(23, 23)
a = b
    
>>> factor_test(9, 11)
No factors here
    
>>> factor_test(7, 28)
a is a factor of b
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def factor_test(a, b):
    result = None
    if a == b:
        result = "a = b"
    elif b % a == 0:
        result = "a is a factor of b"
    elif a % b == 0:
        result = "b is a factor of a"
    else:
        result = "No factors here"

    print(result)

if __name__ == "__main__":
    run_tests()
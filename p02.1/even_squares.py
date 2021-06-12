"""
Problem:

    
The function even_squares takes in a number. If the number is:
    
* even - print out the number squared
    
* odd - print out the number

Tests:

    
>>> even_squares(20)
400
    
>>> even_squares(9)
9
    
>>> even_squares(8)
64
    
>>> even_squares(73)    
73
"""
# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def even_squares(num):
    result = None
    if num % 2 == 0:
        result = num**2
    else:
        result = num

    print(result)

if __name__ == "__main__":
    run_tests()
"""
Problem:

    
The fibonacci numbers start 1, 1, 2, 3, 5, 8, 13, ...
    
The next number in each sequence is given by adding the last
    
two terms.

    
The function fib takes an integer n and should return the
    
nth fibonacci number


Tests:

    
>>> fib(1)
1
    
>>> fib(2)
1
    
>>> fib(5)
5
    
>>> fib(10)  
55
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def fib(n):
    """Non-recursive"""
    num1 = 1
    num2 = 1
    next = 2
    if n == 1:
        print(num1)
    elif n == 2:
        print(num2)
    else:
        for i in range(3, n):
            num1 = num2
            num2 = next
            next = num1 + num2
        print(next)

def fib_rec(n):
    """Recursive solution"""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    run_tests()
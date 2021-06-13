"""
Problem:

    
For part of a game, the players are allowed to use a calculator.
    
We need to implement the part of the code that actually computes the
    
answer when an expression is entered into the calculator.

    
The function 'compute' takes 3 inputs: 2 numbers and an operator.
    
The operator will be either "+", "-" or "x". In each case, the
    
function should print the answer to the expression.

Tests:

    
>>> compute(5, "+", 9)
14
    
>>> compute(7, "+", 12)
19
    
>>> compute(15, "-", 8)
7
    
>>> compute(12, "-", 20)
-8
    
>>> compute(4, "x", 5)
20
    
>>> compute(8, "x", 3)
24
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def compute(x, operator, y):
    if operator == "x":
        print(x * y)
    elif operator == "-":
        print(x - y)
    elif operator == "+":
        print(x + y)

if __name__ == "__main__":
    run_tests()
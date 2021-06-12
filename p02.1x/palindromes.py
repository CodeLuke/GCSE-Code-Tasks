"""
Problem:

    
A palindrome is a number or word that reads the same forwards as backwards,
    
such as "mum", "racecar" or 12321.

    
The function palindromic takes a 3-digit number and should print "Yes"
    
if a number is palindromic, and "No" if it isn't.

Tests:

    
>>> palindromic(121)
Yes
    
>>> palindromic(575)
Yes
    
>>> palindromic(999)
Yes
    
>>> palindromic(234)
No
    
>>> palindromic(741)
No
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def palindromic(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    run_tests()
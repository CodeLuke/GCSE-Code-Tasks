"""
Problem:

   
Professor Odd has developed a very odd system of rounding numbers.
    
    
Like normal rounding, when rounding to the nearest 10 or 100, he looks at
    
the next digit. However, in odd_rounding, if it is zero or odd, he'll round
    
down. If it is bigger than zero and even he'll round up.

    
Example:

    
573 rounded to the nearest 10 is 570, because 3 is odd.
    
429 rounded to the nearest 100 is 500, because 2 is even.
    
390 rounded to the nearest 10 is 390, because it ends in 0.

    
The function odd_rounding takes two numbers: the number to be rounded,
    
and what we want to round to.  
    
We will only round to 10 or 100 for the purposes of this problem, but try
    
and find a general solution for any power of 10.

Tests:

    
>>> odd_rounding(573, 10)
570
    
>>> odd_rounding(572, 10)
570
    
>>> odd_rounding(573, 100)
500
    
>>> odd_rounding(429, 100)
500
    
>>> odd_rounding(790, 10)
790
"""
import doctest, math
def run_tests():
    doctest.testmod(verbose=True)

def odd_rounding(num, tens):
    # Number to check
    num_to_check = int(str(num // tens)[-1])
    result = None
    if num_to_check == 0 or num_to_check % 2 == 1:
        # Replace trailing digits with 0
        result = (num // (tens)) * (tens)
    else:
        # Increment number and then add trailing 0s
        result = (num // (tens) + 1) * (tens)

    print(result)

if __name__ == "__main__":
    run_tests()

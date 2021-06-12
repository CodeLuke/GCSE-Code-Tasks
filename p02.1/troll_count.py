"""
Problem:

    
Many non-trolls stereotypically assume that trolls are illiterate
    
and innumerate.

    
This, like many stereotypes, is untrue.

    
Trolls count like so:  one, two, many, lots ...

    
Where "many" is any number between 3 and 8, and "lots" is any number
    
bigger than 8. The troll_count function takes an integer in, and should
    
print the appropriate troll equivalent.

Tests:
    
>>> troll_count(1)
one
    
>>> troll_count(2)
two
    
>>> troll_count(3)
many
    
>>> troll_count(5)
many
    
>>> troll_count(8)
many
    
>>> troll_count(9)
lots
    
>>> troll_count(12)
lots
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def troll_count(num):
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num >= 3 and num <= 8:
        print("many")
    else:
        print("lots")

if __name__ == "__main__":
    run_tests()
"""
Problem:

    
We need to count the number of vowels present in a string.
    
The function `vowels` should take a string and print out
    
the number of vowels it contains.

Tests:

    
>>> vowels("hello")
2
    
>>> vowels("world")
1
    
>>> vowels("why")
0
    
>>> vowels("beautiful") 
5
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def vowels(word):
    print(sum([1 for char in word if char in "aeiou"]))

if __name__ == "__main__":
    run_tests()
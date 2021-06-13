"""
Problem:

    
The function 'balance' divides a piece of text into two equal halves.
    
For example:  'turtle' -> 'tur' and 'tle'

    
If words have an odd number of characters, it ignores the middle one:
    
For example:  'turtles' -> 'tur' and 'les'

    
Each letter is given a scor
e, A=1, B=2 and so on, and a total score
    
found for each half.

    
If the first half has a greater score, it should print "Start"
    
If the second half has a greater score, it should print "End"
    
If they are the same, it should print "Balanced"


Tests:

    
>>> balance("turtle")
Start
    
>>> balance("elephant")
End
    
>>> balance("gorilla")
Start
    
>>> balance("horse")
End
    
>>> balance("kayak")
Balanced
"""
import doctest
import math
def run_tests():
    doctest.testmod(verbose=True)

def balance(word):
    first_half = word[:len(word)//2]
    second_half = word[math.ceil(len(word)/2):]

    first_score = sum([ord(chr) - ord('a') + 1 for chr in first_half])
    second_score = sum([ord(chr) - ord('a') + 1 for chr in second_half])

    print("Start" if first_score > second_score else "End" if first_score < second_score else "Balanced")

if __name__ == "__main__":
    run_tests()
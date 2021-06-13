"""
Problem:

    
Amazingly, humans can often read words with most of the
    
letters missing from them and still make sense of it.
    
To test this, we will be writing a function that removes
    
every other letter from a piece of text, starting with
    
the second character.

    
For example: 'harmonise' -> 'hrose'

    
Maybe making sense of it isn't so easy after all!

    
Create the function 'reduce'

Tests:

    
>>> reduce('harmonise')
hroie
    
>>> reduce('diplodocus')
dpoou
    
>>> reduce('tyrannosaurus')
trnoars

"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def reduce(word):
    print(word[0::2])

if __name__ == "__main__":
    run_tests()
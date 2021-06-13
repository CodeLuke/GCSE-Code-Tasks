"""
Problem:

    
The function "find" takes in two strings as input, called
    
word and s.  It should search for word in s.

    
If s starts with word - print "Start"
    
If s finished with word - print "End"
    
If word is in the middle somewhere - print "Middle"
    
If word does not appear anywhere- print "Not found"

    
Word will only appear once in s.

    
The search should be case-insensitive.

Tests:

    
>>> find("Hell", "Hello world")
Start
    
>>> find("old", "If I were so bold")
End
    
>>> find("Over", "I would love some dover sole")
Middle
    
>>> find("Piece", "Peter piper picked a peck of pickled pepper")
Not found

"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def find(word, s):
    s = s.lower()
    word = word.lower()

    if s[:len(word)] == word:
        print("Start")
    elif s[len(s) - len(word):] == word:
        print("End")
    elif word in s:
        print("Middle")
    else:
        print("Not found")

if __name__ == "__main__":
    run_tests()
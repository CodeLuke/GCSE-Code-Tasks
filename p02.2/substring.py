"""
Problem:

    
Given a string, s, we can compose a substring using
    
every second letter, starting with the first character.
    
eg. "HelloWorld" -> "Hlool"

    
The function 'sub_search' takes in two strings, s and
    
word.

    If word is present in s - print "Found in original"
    
If word is present in the substring - print "Found in substring"
    
Otherwise, print "Not found"

    
The search should be case-insensitive.

Tests:

    
>>> sub_search("No", "Dont stop me now!")
Found in original
    
>>> sub_search("hag", "I'm having such a good time")
Found in substring
    
>>> sub_search("vin", "Im having a ball")
Found in original
    
>>> sub_search("ago", "If you want to have a good time just give me a call")
Found in substring
    
>>> sub_search("fun", "Dont stop me now!")
Not found
"""

import doctest
def run_tests():
    doctest.testmod(verbose=True)

def sub_search(word, s):
    if word.lower() in s.lower():
        print("Found in original")
    elif word.lower() in s[::2].lower():
        print("Found in substring")
    else:
        print("Not found")

if __name__ == "__main__":
    run_tests()
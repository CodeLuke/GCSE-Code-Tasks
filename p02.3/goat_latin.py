"""
Problem:

    
Goat latin, much like pig latin, is a simple way of encoding words to
    
disguise their meaning.  It works like so:

    
* For small words (3 characters or less), repeat it twice.
      
eg: "and" -> "andand"

    
* For longer words beginning with a vowel, remove the first letter and
    
append it to the end.  eg: "abacus" -> "bacusa"

    
* For longer words beginning with a consonant, reverse them.
    
eg: "world" -> "dlrow"

    
The function encode should take a word, and convert it to its goat latin
    
form. All inputs will be lower case.

    
Hint: print("a" + "b") will print a concatenated (joined up) string.


Tests:

    
>>> encode("it")
itit
    
>>> encode("dob")
dobdob
    
>>> encode("apple")
pplea
    
>>> encode("rhubarb")
brabuhr
    
>>> encode("orange")
rangeo
    
>>> encode("pineapple")
elppaenip
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def encode(plaintext):
    if len(plaintext) <= 3:
        print(plaintext + plaintext)
    elif plaintext[0] in "aeiou":
        print(plaintext[1:] + plaintext[0])
    else:
        print(plaintext[::-1])

if __name__ == "__main__":
    run_tests()
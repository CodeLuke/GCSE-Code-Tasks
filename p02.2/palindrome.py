"""
Problem:

    
A palindrome is a word that is spelt the same forwards as it is
    
backwards, such as "racecar" or "mum".

    
The function 'is_palindrome' should test whether a word is a
    
palindrome or not and print either "Palindrome" or "Non-palindrome"

    
The function should be case-insensitive, so "Racecar" should still
    
be counted as a palindrome.

Tests:

    
>>> is_palindrome("racecar")
Palindrome
    
>>> is_palindrome("RaceCar")
Palindrome
    
>>> is_palindrome("AManAPlanACanalPanama")
Palindrome
    
>>> is_palindrome("Test")
Non-palindrome
    
>>> is_palindrome("Aloha")
Non-palindrome
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def is_palindrome(word):
    """Conventional, imperative version"""
    backwards_word = ""
    for i in range(len(word) - 1, -1, -1):
        backwards_word += word[i]
    
    if word.lower() == backwards_word.lower():
        print("Palindrome")
    else:
        print("Non-palindrome")
    

def is_palindrome_oner(word):
    """One line version"""
    print("Palindrome" if word.lower() == word[::-1].lower() else "Non-palindrome")

if __name__ ==  "__main__":
    run_tests()
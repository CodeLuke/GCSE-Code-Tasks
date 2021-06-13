"""
Problem:

    
The function 'isCap' takes a string, and an integer, n.  

     
* If the nth character (starting with the first as character 0) in the 
       
string is a capital, it should print "Capital".
     
     
* If it is not a capital, it should print "Non-capital".
      
     
* If there is no such letter, because the string is too small, it should
       
print "Too small"



Tests:

    
>>> isCap("Test", 0)
Capital
    
>>> isCap("Test", 2)
Non-capital
    
>>> isCap("Another", 6)
Non-capital
    
>>> isCap("TEST", 3)
Capital
    
>>> isCap("", 2)
Too small
    
>>> isCap("Hooray", 6)
Too small
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def isCap(string, index):
    if len(string) <= index:
        print("Too small")
    elif string[index].isupper():
        print("Capital")
    else:
        print("Non-capital")

if __name__ == "__main__":
    run_tests()

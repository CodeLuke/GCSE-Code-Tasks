"""
Problem:

    
The function 'test_case' takes a string and should
    
return whether that string is upper case, lower
    
case or a mixture of upper and lower case 
    
characters. It should print "Upper", "Lower" or
    
"Mixed".


Tests:

    
>>> test_case("a lower case string")
Lower
    
>>> test_case("AN UPPER CASE STRING")
Upper
    
>>> test_case("A mixed CASE string")    
Mixed
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def test_case(string):
    has_upper = False
    has_lower = False
    for char in string:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        # Optimisation to break if already decided is mixed
        if has_lower and has_upper:
            break;
    
    if has_upper and not has_lower:
        print("Upper")
    elif has_lower and not has_upper:
        print("Lower")
    else:
        print("Mixed")

if __name__ == "__main__":
    run_tests()
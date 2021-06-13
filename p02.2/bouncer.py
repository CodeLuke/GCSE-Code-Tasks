"""
Problem:

    
Elton John is holding a party for a small selection of his many friends.
    
Unfortunately, word of this has got round and lots of other people are
    
trying to gatecrash.

    
Elton has had to employ a bouncer to check whether people are on the
    
guest list or not. The last two people to arrive are Elizabeth Hurley
and Victoria Beckham.

    
The function guestlist takes a name (a string). If it is either 
    
"Elizabeth Hurley" or "Victoria Beckham", it should print "Come on in",
    
otherwise it should print "You're not on the list - scram!"


Tests:

    
>>> guestlist("Victoria Beckham")
Come on in!
    
>>> guestlist("Elizabeth Hurley")
Come on in!
    
>>> guestlist("Donald Trump")
You're not on the list - scram!
    
>>> guestlist("Tom Cruise")
You're not on the list - scram!
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def guestlist(guest_name):
    if guest_name == "Elizabeth Hurley" or guest_name == "Victoria Beckham":
        print("Come on in!")
    else:
        print("You're not on the list - scram!")

if __name__ == "__main__":
    run_tests()
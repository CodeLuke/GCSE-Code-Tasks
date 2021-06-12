{-
Problem:
    
Bob would like to buy some sweets, which cost 50p.
    
Bob has some money but, unfortunately, Bob is only 3
    
and has no concept of money yet. Bob's solution to this
    
is to just hand over the whole of his change and hope the
    
shopkeeper will sort it out for him.
    
The function bobs_change takes in a number representing
    
how much money Bob has handed over (in pence). It should print
    
the amount of change owed if he has enough, or
    
"Sorry Bob, you don't have enough" if he is short.
Tests:
    
>>> bobsChange(80)
"30"
    
30
    
>>> bobsChange(132)
"82"
    
82
    
>>> bobsChange(50)
"0"
    
0
    
>>> bobsChange(40)
"Sorry Bob, you don't have enough"
    
Sorry Bob, you don't have enough
-}

module BobsChange where

sweetCost = 50 -- price of sweets in pence

bobsChange :: Integer -> String
bobsChange change  =
    let priceDiff = change - sweetCost
    in if priceDiff >= 0
       then show priceDiff
       else "Sorry Bob, you don't have enough"

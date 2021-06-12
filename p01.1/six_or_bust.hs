
-- |Problem:
-- |A desperate gambler has bet all of his money on a final last throw of the die.
-- |If he rolls a six, he survives to fight another day.    
-- |Anything else, and he gets thrown to the thugs waiting for him in the back alley.
-- |The goneBust function takes an integer n, and should print either "Pheww!" or
-- |"HELP! HELP!" depending on whether he survives or not.
--
-- Tests:
-- >>> goneBust(2)
-- "HELP! HELP!"
--    
-- >>> goneBust(6)
-- "Pheww!"
--    
-- >>> goneBust(10)    
-- "HELP! HELP!"


module GoneBust where

goneBust :: Integer -> String  
goneBust roll = 
    if roll == 6
        then "Pheww!"
        else "HELP! HELP!"

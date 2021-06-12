"""
    'In this world nothing can be said to be certain, except death and taxes.'

                                                - Benjamin Franklin

Problem:

    
The percentage of your income that you pay as tax varies in the UK
    
depending on your income (numbers are slightly simplified here):

    
* If you earn £10,000 or less, you pay no tax.

    
* If you earn over £10,000, you pay 20% on the money you earn over
      
£10,000, up to £40,000.

    
* If you earn over £40,000, you pay 40% on all the money you earn over
      
£40,000.

    
For example, if someone earns £50,000 they will pay:
    
    
* Nothing on the first £10,000
    
* 20% on the next £30,000 = £6,000
    
* 40% on the next £10,000 = £4,000

    
In total, they would pay £10,000 tax.

    
The function tax takes an amount of earnings as an input and should print
    
out the amount of tax payable.

    
All inputs will be divisible by 10, and your answer should be a whole
    
number.



Tests:

    
>>> tax(8000)    
0

>>> tax(15000)
1000
    
>>> tax(32000)
4400
    
>>> tax(48000)
9200
    
>>> tax(100000) 
30000
"""
import doctest
import math
def run_tests():
    doctest.testmod(verbose=True)

def tax(income):
    payable = 0
    if income > 40000:
        payable += 0.4 * (income - 40000) + 0.2 * (30000)
    elif income > 10000:
        payable += 0.2 * (income - 10000)
    
    return math.floor(payable)


def tax_rec(income):
    """
    A more advanced implementation that uses recursion
    """
    payable = 0
    if income > 40000:
        payable = 0.4 * (income - 40000) + tax_rec(40000)
    
    elif income > 10000:
        payable = 0.2 * (income - 10000)
    
    return math.floor(payable)

if __name__ == "__main__":
    run_tests()
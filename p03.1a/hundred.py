"""
Problem:

    The function add_100 should add all the numbers from
    1 to 100 and print the total.

    The function contains the first few lines of a (very poor)
    implementation but whoever wrote it clearly got bored and
    gave up with their attempts.

    Rewrite and finish it using a loop.


Test:

    >>> add_100()
    5050

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def add_100():
    total = 0
    for i in range(1,101):
        total = total + i

    print(total)

if __name__ == "__main__":
    run_tests()
# Iteration with Strings - Extension Problems

## Problem Check-list

  * [ ] odd_letters
  * [ ] word_balance
  * [ ] caesar


## ASCII Code.

To solve some of the problems in this extension set, you may find it useful to
give each letter a number at times. A = 1 etc.

One way of doing this is to make use of something called ASCII codes.
ASCII is used to encode the different characters we see on screen into binary
for storing on disk.

The letter 'A' for instance is equivalent to 65 in ASCII, which translates to
01000001 when written as an 8-bit binary number.

In python, we can translate from ASCII and back using the `ord` and `chr` 
functions:

``` python

    >>> ord('A')
    65
    >>> chr(65)
    'A'

```

A table of ascii codes and values are included below:

![ascii](ascii-table.png)

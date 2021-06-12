# Iteration with Integers and Range

## Problems Check-list

* [ ] nines
* [ ] more_nines
* [ ] hundred
* [ ] hundred_or_more

## Notes

Iteration is the computer science word for repeating a process again and again. This problem set
looks at iterating (sometimes referred to as 'looping') using a `for` loop, and a numerical `range`.

### Simple looping

If I just want to repeat the same process multiple times, the syntax is very simple:

``` python
for i in range(5):
	print("Hello world 5 times!")
```

The number specified with the range tells us how many times we're repeating something, whilst
anything following that and indented will be repeated.  Moving the indentation back will tell
python that we no longer want to loop things.

``` python
for i in range(5):
	print("Hello world 5 times!")

print("Bye just once, because it's not in the loop!")
```

### Using the iteration variable

What is actually happening when we iterate is a little more complex:
  * A variable is created - this is what we specify in the `for i in` bit
  * It sets the variable, in this case `i`, to the first number in our range.
  * It carries out the instructions with that value of `i`.
  * It then changes the variable to the next number in the range and then repeats.

We can see this if we were to run:

``` python
>>> for i in range(5):
>>>		print(i)
0
1
2
3
4
```

range(5) produces the numbers 0 to 4 (more on this later). The for loop goes through each
of these numbers and runs the indented code with `i` set to that number; in this case, just
printing it.


### Specifying what to range over.

Python's `range` allows us to create sequences of numbers to iterate over.  It can be used
with 1, 2 or 3 variables and each means something slightly different:

#### range(stop)

The numbers from 0 to 'stop' (not including 'stop'):

`range(7)` = 0, 1, 2, 3, 4, 5, 6

#### range(start, stop)

The numbers from 'start' to 'stop' (including 'start' but not 'stop'):

`range(3, 8)` = 3, 4, 5, 6, 7

#### range(start, stop, step)

Just as before, but this time going up by 'step' each time. If 'step' is negative, it
will create a countdown:

`range(8, 4, -1)` = 8, 7, 6, 5


### Counts, Sums and Products

It is o often useful to create a count of the number of items in our loop, or add them
all up, or multiply them all.

This can be achieved like so:

``` python
count = 0
for i in range(1, 11):
	count = count + 1

print(count)
```

Here we create a variable at the start to store our count. On each iteration we update
our variable, adding 1 to it each time.

If instead we want to create a total, we could use `total = total + n` inside our loop.

Finding a product is very similar: `product = product * n`


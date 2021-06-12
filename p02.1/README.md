# Problems

- [ ] hit_100 
- [ ] even_squares
- [ ] roll_double
- [ ] university_challenge
- [ ] factor_test
- [ ] biggest
- [ ] fizzbuzz
- [ ] troll_count


# Conditionals - If/Elif/Else

## Basics

All of these problems require the use of conditionals.
This is how our code makes decisions.
In python, the syntax to do this looks like:

``` python
	if some criteria:
		do something
```

For example:

``` python
	if x == 5:
		print("x is 5!")
```

Important points:
  * When asking whether two things are equal, we use a double equals `==`
  * Our if statement must end in a colon `:`
  * The code we want to execute if the condition is true must be indented.
	We finish this block of code by moving the indentation back out.

## Checking multiple conditions

If there are multiple options we want to check within the same decision block
we can use `if`, `elif`, and `else` conditions.  We must start with `if`, can have
as many `elif` statements as we want and can, optionally, catch everything
else with an `else` statement at the very end.

Example:

``` python

if x == 5:
	print("x is 5")

elif x >= 5:
	print("x is bigger than 5")

elif x > 0:
	print("x must be greater than 0 and less than 5")

else:
	print("x must be 0 or less")

```

By using `elif` and `else` we will only get to later statements if the earlier
ones are not true.  This is how we know, by the third statement (`elif x > 0`),
that x must be between 0 and 5 - if x was 5 or bigger we would never have got
to this point in the code.

## More advanced conditions

We can use the keywords `and` and `or` if we need to test multiple conditions
together on one line.

Example:

``` python

if x > 10 and x <= 20:
	print("bigger than 10 but less than or equal to 20")

```

Note: The conditions either side of an `and` or `or` have to be full questions.


# Integer conditions

Some useful tests we can use with integers are:

* `x == a` - x equal to a
* `x > a` - x greater than a
* `x < a` -  x less than a
* `x >= a` - x greater than or equal to a
* `x <= a` -  x less than or equal to a
* `a < x < b` - x between a and b (we can use `<=` in here as well)

Another very useful test to use is to check whether something is divisible:

* `x % 2 == 0` - test if x is divisible by 2


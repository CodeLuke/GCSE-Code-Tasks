# Iteration with Strings

## Problem Check-list

  * [ ] double_letters
  * [ ] vowel_count
  * [ ] only_consonants
  * [ ] word_scorer
  * [ ] position_sum


## Iterating through each character in a string

If we want to look at each character in a string and do something with it,
we can loop through them like so:

``` python
for char in range(some_string):
    
    ... do something with char
```

This creates a new variable, char, and assigns it to each of the characters
in our string in turn.  We can then do something with each of these characters.

For example, if I wanted to remove all of the letter 'e' present in a string,
I could do:

``` python

input_string = "Hello, where are all the eees"
output_string = ""

for char in input_string:
    if char != "e":
        output_string = output_string + char

print(outout_string)

```

This code loops through each character in 'input_string' and, assuming the
character is not an 'e', adds it to output_string.  It will print out:
"Hllo, whr ar all th s".


## Iterating where we need to know the position of a character.

If we need to know the position of a character, we can use the length of the
string and an iteration over a range instead:

``` python
some_string = "Hello world"
length = len(some_string)

for n in range(length):
    
    ... do something with some_string[n]
```

For example, if I wanted to print the locations of each "o", I could do:

``` python

some_string = "Hello world"
length = len(some_string)

for n in range(length):

    if some_string[n] == "o":
        print(n)

```

The difference here is that we need to use `some_string[n]` rather than `char`.






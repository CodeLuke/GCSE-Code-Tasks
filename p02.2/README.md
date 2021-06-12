# Conditionals with Strings

## Problem Check-list

- [ ] bouncer
- [ ] targets
- [ ] word_finder 
- [ ] mixed_case
- [ ] dictionary_corner
- [ ] number_sort 
- [ ] palindrome 
- [ ] substring


## Useful String Conditions

### Equals and inequalities

We can test whether strings are equal just like integers using `==`.

If we want to test whether strings would be before or after each other
in the dictionary, we can use `>`, `>=`, `<` and `<=`:

``` python
	if "Apple" < "Banana":
		print("Apple is before Banana")
```

However, be careful because **case** is important here. If we try:

``` python
	if "apple" > "Banana":
		print("apple is after Banana")
```

This will print "apple is after Banana".  This is because strings are case
sensitive and the lower-case alphabet comes after the upper case alphabet.

### Case

To change the case of a string, we can use the methods::
  * `"My stRiNg".upper()			# "MY STRING"`
  * `"My stRiNg".lower()			# "my string"`
  * `"My stRiNg".title()			# "My String"`
  * `"My stRiNg".capitalalize()		#"My string"`

This is useful to, amongst other things, check whether two strings are the
same without worrying about case:

``` python

	if "Apple".lower() == "aPPLe".lower():
		print("Same word, potentially different case")

```

We can also check the case of a word using the methods:
  * `"my string".isupper()		# False`
  * `"my string".islower()		# True`
  * `"My String".istitle()		# True`

``` python
	if "my string".islower():
		print("That's a lowercase string!")
```

### String length

We can find the length of a string (the number of characters, including spaces),
easily by using the `len` function:

``` python
	s = "A string with many words!"
	if len(s) > 10:
		print("That's a long word!")
```

### Characters and substrings

*Splicing* a string into its constituent characters and substrings is easily
achieved using square brackets and operates much like the `range` object for
numbers. Remember that counting starts at 0 here.

``` python
	s = "My example string"
	#	 01234567890123456   - The character numbers (the second 0 = 10 and so on)

	print(s[0])					# M - the first character.
	print(s[4])					# x - the 5th character
	print(s[-2])				# n - the second last character

	print(s[3:7])				# exam - characters 3 to 6
	print(s[11:])				# string - character 11 onwards
	print(s[:10])				# My example - characters up to character 9.
	
	print(s[0:10:2])			# 'M xml' - every second character from 0 to 9
	print(s[::-1])				# 'gnirts selpmaxe yM' - all characters in reverse order
```

### Checking for prefixes/suffixes/substrings

If we would like to check whether a string starts or finishes with a
particular character or substring, we can use the methods:

	* `"My string".startswith("My")		# True`
	* `"My string".endswith("ring")		# True`

The keyword `in` will also allow us to check for substrings:

``` python
	s = "My example string"
	if "exam" in s:
		print("Found 'exam' in the string")

```



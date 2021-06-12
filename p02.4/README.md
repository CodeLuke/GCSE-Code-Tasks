# Conditionals with Lists

## Problem Checklist

  * [ ] ends
  * [ ] unique_insert
  * [ ] repeater
  * [ ] pig_list
  * [ ] most_frequent
  * [ ] clean_sweep



## Notes

### Basics

A list is created by wrapping a set of elements (integers, strings etc.) in square brackets:

``` python
my_list = [1, 2, "A", "hello", 3.14, True]
```

The items in the list *do not have to be* the same type, but in most cases they will be.

We can access items in our list just like characters in a string, using their index (position)
in the list:

``` python
my_list = [1, 2, 3, 4]
my_list[0]              # The first item in the list = 1
my_list[2]              # The third item in the list = 3
my_list[-1]             # The last item in the list = 4
```

We can add things to a list by either appending or inserting:

``` python
my_list = [1, 2, 4]
my_list.insert(2, 3)    # Insert '3' at position 2 - moving the 4 back.
my_list.append(5)       # Add 5 to the end of the list.
```

We can remove things, either by their position or value:

``` python
my_list = [1, 2, 3, 4]
my_list.pop(0)              # Pop will remove the item at that position, in this case the first item.
my_list.remove(3)           # Remove the first occurence of '3' in the list.

x = my_list.pop(0)          # If we want to use the value of an item we've popped
                            # from the list, we can assign it to a variable.
```


### Conditionals

If we want to know how long a list is, we can the use the `len` function:

``` python
my_list = [1, 2, 3, 4]
length = len(my_list)
```

If we want to know whether an item exists in our list, we can use the `in` keyword:

``` python
my_list = [1, 2, 3, 4]
if 3 in my_list:
    print("3 is in the list")
```

If we would like to know how many times an item appears in the list, we can `count` it:

``` python
my_list = [1, 2, 3, 4, 3, 2, 1, 2, 3, 3]
threes = my_list.count(3)
```



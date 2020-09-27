#List Comprehensions to combine elements of multiple lists

Example: start with a list of lists, each of len(3):
```
# a list of lists, each three items long.
old_list = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	]
```
	
You can use list comprehensions to selectively add items from `old_list` to a new list:
```	
first_items = [x[0] for x in old_list]
second_items = [x[1] for x in old_list]
third_items = [x[2] for x in old_list]
```
You can filter the comprehension using a conditional statement:
```
some_first_items = [
    x[0] for x      #the 0th element...
    in old_list     # of of each list in old_list
    if x[0] > 1     # if that element is > 1.
    ]
```

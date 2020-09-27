# Using zip() to combine iterables

Example: Start with three lists: 
```
[x,x,x], [y,y,y], [z,z,z]
```
End with:
```
[x,y,z], [x,y,z], [x,y,z]
```

How to do it:
```
list1 = [1, 1, 1]
list2 = [2, 2, 2]
list3 = [3, 3, 3]

# use zip() to create a zip iterable that we can iterate over: each iteration will be a tuple of the next values in each of the source lists
zip_object = zip(list1, list2, list3)
for i in zip_object:
	print(i) # or do something more useful...
```

We can shorten the above to:

```
for i in zip(list1, list2, list3):
	print(i)
```
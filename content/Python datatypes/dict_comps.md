# Dictionary comprehension

## Basic syntax:

`k:v for k, v in some_dict}`

## Explanation
It's common to loop through a dict by doing this:
```
for k, v in some_dict.items():
    # do something...
```

A dictionary comprehension simply adds an extra layer of syntax:

```
new_dict =          # assign the result of the comprehension to a new dict variable
{                   # wrap the expression in curly brackets, because we're making a dict
    k:v             # add a new key:value pair to the new dict... 
    for k, v        # for each key:value pair...
    in some_dict    # in the source dict.
}
```

## Adding conditions

We can choose to only add a key:value pair from the old dict to the new dict if certain conditions apply:
```
new_dict =                  # assign the result of the comprehension to a new dict variable
{                           # wrap the expression in curly brackets, because we're making a dict
    k:v                     # add a new key:value pair to the new dict... 
    for k, v                # for each key:value pair...
    in some_dict.items()    # in the source dict
    if k > 5                # but only if the value of the key is greater than 5.
}
```

We can also test the condition of the value in each key:value pair:

```
new_dict =                  # assign the result of the comprehension to a new dict variable
{                           # wrap the expression in curly brackets, because we're making a dict
    k:v                     # add a new key:value pair to the new dict... 
    for k, v                # for each key:value pair...
    in some_dict.items()    # in the source dict...
    if v.some_property      # but only if the object stored as the value's property some_property evaluates to True.
}
```

We can also transform the key:value pair going into the new dict:
```
new_dict =                  # assign the result of the comprehension to a new dict variable
{                           # wrap the expression in curly brackets, because we're making a dict
    k:v* 2                  # add a new key:value pair to the new dict, whith the value being twice the original... 
    for k, v                # for each key:value pair...
    in some_dict.items()    # in the source dict.
}
```

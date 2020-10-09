# Use rsplit() to get the last section of a path

If we have a path as a string:
`path_string = "/some/path/to/a/file/somefile.txt"`

We might want to capture just the portion of the string after the final forward slash. We can't use `.split("/")` if we want to keep the path intact - that would split on every forward slash.

Instead, we can use `rsplit()` which works like `split()` except that it starts reading from the end of the string. We can pass a second argument to tell it how many splits to perform.

`path_string.rsplit("/", 1)` will return: `["/some/path/to/a/file","somefile.txt"]`
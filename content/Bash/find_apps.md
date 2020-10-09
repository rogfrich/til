# Find all apps installed on a Mac

`sudo find / -iname '*.app' > /path/to/output/folder/output.txt`

Explanation:

```
sudo                                    # Running as superuser
find                                    # search the supplied path...
/                                       # ...which is everything in root (i.e. everything)
-iname                                  # matching on name, case insensitive (-name would be case sensitive)
'*.app'                                 # find any file that matches the expression '*.app' 
> /path/to/output/folder/output.txt`    # write the output to a file.
```
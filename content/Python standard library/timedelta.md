# Getting the difference between two datetime objects

```
import datetime

today = datetime.datetime.now()
some_time_ago = datetime.datetime(2019, 12, 1, 13, 22, 3)

difference = (today - some_time_ago)
print(difference)
print(type(difference))
```
The code above returns this output:
```
296 days, 7:07:57.681336
<class 'datetime.timedelta'>
```
There were 296 days, 7 hours, 7 minutes and 57.681336 seconds between the moment the code ran and the date specified in `some_time_ago`

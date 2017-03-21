# common-utils
It's one utils library of Python, which includes some common funcitons, but not in Python Standard Library

# Examples:
1. paginate
```javascript
from common.utils.page_utils import paginate


data = list(range(1, 100, 1))

for page in paginate(data, 10):
  print("%r" % page)
```

2. drange
```javascript
from common.utils.datetime_utils import drange
from datetime import datetime, timedelta

start = datetime.now()
stop = start + timedelta(days=10)

for d in drange(start, stop, hours=10):
  print(d)
````

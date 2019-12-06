# Numpy
### Indexing and slicing 
```python
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
arr[:2,]

# result
# array([[1,2,3],[4,5,6]])

arr[:1,:2]

# result
# array([[1,2]])

```

### Boolean Indexing
```python
arr = np.array([[11,22],[21,22],[31,32]])
print(arr)

# result 
# [[11 12][21 22][31 32]]

filter = (arr > 15)
filter

# result
# array([[ False, False],[True, True],[True, True]], dtype=bool)

print(arr[filter])

arr[(arr > 20 & arr < 30)]

arr[(arr % 2 == 0)]

arr[arr % 2 == 0] += 100
```

# DataFrame
### add column names
``` python
import pandas as pd
import numpy as np

test_data = np.array([[1,2,3],[4,5,6])

df = pd.DataFrame(test_data, columns=['col1','col2','col3'])
```

### extract to csv
- with index number
```python
import pandas as pd

pd.to_csv('aaa.csv')
```
- without index number
```python
import pandas as pd

pd.to_csv('aaa.csv', index=False)
```

# How to deal with data using python

### csv 

```python
import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
```

### dictionary

```python
# init
dict_profile = {'name':'Jason', 'gender':'male', 'age':'39'}
dict_profile['gender'] = dict_profile['gen']

# add 
dict_profile['city':'Seoul']

# delete
del(dict_profile['gen'])
```

### set method
provide functions to make set

```python
set1 = set([1,2,3,4])

print(set1)

{1,2,3,4}
```

### Manipulating Datetime 
```python
import datetime

dt = datetime.datetime.strptime("2019-12-02T09:10:05-0500","%Y%m%d%H%M%S")
dt
``` 

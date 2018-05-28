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

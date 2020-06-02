---
layout:     post
title:      "Leetcode array类型整理 part6"
subtitle:   " \"Python Leetcode整理\""
date:       2019-02-21 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## virtualenv

1. Create a virtual environment for a project:

```
$ cd project_folder
$ virtualenv venv
```

virtualenv venv will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was venv) can be anything; omitting the name will place the files in the current directory instead.

2. To begin using the virtual environment, it needs to be activated:

```
$ source venv/bin/activate
```

3. If you are done working in the virtual environment for the moment, you can deactivate it:
```
$ deactivate
```

4. Use the requirement file:

In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages.

```
$ pip freeze > requirements.txt
```

```
$ pip install -r requirements.txt
```

## Structuring Your Project

### Sample Repository

```
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```

## Code Style

### Explicit code

Bad:

```
def make_complex(*args):
    x, y = args
    return dict(**locals())
```

Good:

```
def make_complex(x, y):
    return {'x': x, 'y': y}
```

In the good code above, x and y are explicitly received from the caller, and an explicit dictionary is returned. The developer using this function knows exactly what to do by reading the first and last lines, which is not the case with the bad example.

### One statement per lines

Bad:

```
print 'one'; print 'two'

if x == 1: print 'one'

if <complex comparison> and <other complex comparison>:
    # do something
```

Good:

```
print 'one'
print 'two'

if x == 1:
    print 'one'

cond1 = <complex comparison>
cond2 = <other complex comparison>
if cond1 and cond2:
    # do something
```

### Function arguments

1. Positional arguments

are mandatory and have no default values. They are the simplest form of arguments and they can be used for the few function arguments that are fully part of the function’s meaning and their order is natural. For instance, in send(message, recipient) or point(x, y) the user of the function has no difficulty remembering that those two functions require two arguments, and in which order.

2. Keyword arguments

are not mandatory and have default values. They are often used for optional parameters sent to the function. When a function has more than two or three positional parameters, its signature is more difficult to remember and using keyword arguments with default values is helpful. For instance, a more complete send function could be defined as send(message, to, cc=None, bcc=None). Here cc and bcc are optional, and evaluate to None when they are not passed another value.

3. Arbitrary argument List

is the third way to pass arguments to a function. If the function intention is better expressed by a signature with an extensible number of positional arguments, it can be defined with the \*args constructs. In the function body, args will be a tuple of all the remaining positional arguments. For example, send(message, \*args) can be called with each recipient as an argument: send('Hello', 'God', 'Mom', 'Cthulhu'), and in the function body args will be equal to ('God', 'Mom', 'Cthulhu').


4. Arbitrary keyword argument dictionary

is the last way to pass arguments to functions. If the function requires an undetermined series of named arguments, it is possible to use the \**kwargs construct. In the function body, kwargs will be a dictionary of all the passed named arguments that have not been caught by other keyword arguments in the function signature.

### Avoid the migical wand

### Returning values

In order to keep a clear intent and a sustainable readability level, it is preferable to avoid returning meaningful values from many output points in the body.

```
def complex_function(a, b, c):
    if not a:
        return None  # Raising an exception might be better
    if not b:
        return None  # Raising an exception might be better
    # Some complex code trying to compute x from a, b and c
    # Resist temptation to return x if succeeded
    if not x:
        # Some Plan-B computation of x
    return x  # One single exit point for the returned value x will help
              # when maintaining the code.
```

### Idioms

1. Unpacking

If you know the length of a list or tuple, you can assign names to its elements with unpacking.

```
for index, item in enumerate(some_list):
    # do something with index and item
```

You can use this to swap variables as weell:

```
a, b = b, a
```

Nested unpacking works too:

```
a, (b, c) = 1, (2, 3)
```

```
a, *rest = [1, 2, 3]
# a = 1, rest = [2, 3]
a, *middle, c = [1, 2, 3, 4]
# a = 1, middle = [2, 3], c = 4
```

### Create an ignored variable

```
filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')
```

### Create a length-N list of the same anything

```
four_nones = [None] * 4
```

### Create a length-N list of lists

```
four_lists = [[] for __ in xrange(4)]
```

### Create a string from a lists

```
letters = ['s', 'p', 'a', 'm']
word = ''.join(letters)
```

### Access a Dictionary element

Bad:

```
d = {'hello': 'world'}
if d.has_key('hello'):
    print d['hello']    # prints 'world'
else:
    print 'default_value'
```

Good:

```
d = {'hello': 'world'}

print d.get('hello', 'default_value') # prints 'world'
print d.get('thingy', 'default_value') # prints 'default_value'

# Or:
if 'hello' in d:
    print d['hello']
```

### Short Ways to Manipulate lists

Bad:

```
# needlessly allocates a list of all (gpa, name) entires in memory
valedictorian = max([(student.gpa, student.name) for student in graduates])
```
Good:

```
valedictorian = max((student.gpa, student.name) for student in graduates)
```


### Filtering a list

Bad:

```
# Filter elements greater than 4
a = [3, 4, 5]
for i in a:
    if i > 4:
        a.remove(i)
```

Good:

```
# comprehensions create a new list object
filtered_values = [value for value in sequence if value != x]

# generators don't create another list
filtered_values = (value for value in sequence if value != x)
```

### Modifying the values in a list

Bad:

```
# Add three to all list members.
a = [3, 4, 5]
b = a                     # a and b refer to the same list object

for i in range(len(a)):
    a[i] += 3             # b[i] also changes
```

Good:
```
a = [3, 4, 5]
b = a

# assign the variable "a" to a new list without changing "b"
a = [i + 3 for i in a]
```

### Read From a File

Bad:

```
f = open('file.txt')
a = f.read()
print a
f.close()
```

Good:

```
with open('file.txt') as f:
    for line in f:
        print line
```

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

## Test Your Code

Creating test cases is accomplished by subclassing unittest.TestCase.

```
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
```

The doctest module searches for pieces of text that look like interactive Python sessions in docstrings, and then executes those sessions to verify that they work exactly as shown.

```
def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

## Logging

Logging serves two purposes:

**Diagnostic logging** records events related to the application’s operation. If a user calls in to report an error, for example, the logs can be searched for context.
**Audit logging** records events for business analysis. A user’s transactions can be extracted and combined with other user details for reports or to optimize a business goal.

## Common Gotchas

### Mutable Default argument

Python’s default arguments are evaluated once when the function is defined, not each time the function is called (like it is in say, Ruby). This means that if you use a mutable default argument and mutate it, you will and have mutated that object for all future calls to the function as well.

### Late Binding Closures

Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called.

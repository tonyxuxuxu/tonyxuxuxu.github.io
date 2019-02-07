---
layout:     post
title:      "Python中Map， Filter和Reduce的使用"
subtitle:   " \"Python中一些特别技巧整理\""
date:       2019-02-06 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
---


## Map

Map applies a function to all items in an input_list.

`map(function_to_apply, list_of_inputs)`

Most of the times we want to pass all the list elements to a function one-by-one and then collect the output.

```
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

Map in Python 3 is equivalent to this:
```
def map(func, iterable):
   for i in iterable:
       yield func(i)
```

## Filter

Filter creates a list of elements for which a function return true. The filter resembles a for a loop but it is a builtin function and faster.

```
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x<0, number_list))
```
## Reduce

Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list.

```
from functools import Reduce
product = reduce((lambda x, y: x*y), [1, 2, 3, 4])
```

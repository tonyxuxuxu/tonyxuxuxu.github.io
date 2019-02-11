---
layout:     post
title:      "Python中yield和generator"
subtitle:   " \"Python中一些特别技巧整理\""
date:       2019-02-06 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
---
## *yield* keyword

The *yield* keyword in Python is used to create generators. A generator is a type of collection that produces items on-the-fly and can only be iterated once. By using generators you can improve your application's performance and consume less memory as compared to normal collections, so it provides a nice boost in performance.

*return* statement:
```
def cub_number(nums):
   cube_list = []
   for i in nums:
       cube_list.append(i**3)
   return cube_list
```

*yield* statement:
```
def cub_number(nums):
   for i in nums:
       yield(i**3)
```
In the above script, the cube_numbers function returns a generator instead of list of cubed number. It's very simple to create a generator using the *yield* keyword. Here we do not need the temporary cube_list variable to store cubed number, so even our cube_numbers method is simpler. Also, no return statement is needed, but instead the *yield* keyword is used to return the cubed number inside of the for-loop.

Now, when *cub_number* function is called, a generator is returned. It doesn't actually execute at this point in time, and there are not any items in memory.

To get the function to execute, and therefore the *next* item from generator, we use the built-in *next* method. When you call the *next* iterator on the generator for the first time, the function is executed until the *yield* keyword is encountered. Once *yield* is found the value passed to it is returned to the calling function and the generator function is paused in its current state.

`next(cubs)`

The above function will return "1". Now when you call *next* again on the generator, the *cube_numbers* function will resume executing from where it stopped previously at *yield*. The function will continue to execute until it finds *yield* again. The *next* function will keep returning cubed value one by one until all the values in the list are iterated.

Once all the values are iterated the *next* function throws a StopIteration exception. It is important to mention that the cubes generator doesn't store any of these items in memory, rather the cubed values are computed at runtime, returned, and forgotten. The only extra memory used is the state data for the generator itself, which is usually much less than a large list. This makes generators ideal for memory-intensive tasks.

Instead of always having to use the *next* iterator, you can instead use a "for" loop to iterate over a generators values. When using a "for" loop, behind the scenes the next iterator is called until all the items in the generator are iterated over.

## generators

A generator "generates" values. Creating generators was made as straightforward as possible through the concept of generator functions, introduced simultaneously.

A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the *yield* keyword rather than return. If the body of a def contains *yield*, the function automatically becomes a generator function (even if it also contains a return statement). There's nothing else we need to do to create one.

generator functions create generator iterators. That's the last time you'll see the term generator iterator, though, since they're almost always referred to as "generators". Just remember that a generator is a special type of iterator. To be considered an iterator, generators must define a few methods, one of which is `__next__()`. To get the next value from a generator, we use the same built-in function as for iterators: *next()*.

This point bears repeating: to get the next value from a generator, we use the same built-in function as for iterators: *next()*.



(next() takes care of calling the generator's `__next__()` method). Since a generator is a type of iterator, it can be used in a for loop.

So whenever next() is called on a generator, the generator is responsible for passing back a value to whomever called *next()*. It does so by calling yield along with the value to be passed back (e.g. yield 7). The easiest way to remember what yield does is to think of it as return (plus a little magic) for generator functions.

### example:

```
>>> def simple_generator_function():
>>>    yield 1
>>>    yield 2
>>>    yield 3
```

```
>>> for value in simple_generator_function():
>>>     print(value)
1
2
3
>>> our_generator = simple_generator_function()
>>> next(our_generator)
1
>>> next(our_generator)
2
>>> next(our_generator)
3
```

When a generator function calls *yield*, the "state" of the generator function is frozen; the values of all variables are saved and the next line of code to be executed is recorded until *next()* is called again. Once it is, the generator function simply resumes where it left off. If *next()* is never called again, the state recorded during the yield call is (eventually) discarded.

If a generator function calls return or reaches the end its definition, a `StopIteration` exception is raised. This signals to whoever was calling *next()* that the generator is exhausted (this is normal iterator behavior). It is also the reason the `while True`: loop is present in `get_primes`. If it weren't, the first time *next()* was called we would check if the number is prime and possibly yield it. If *next()* were called again, we would uselessly add 1 to number and hit the end of the generator function (causing `StopIteration` to be raised). Once a generator has been exhausted, calling *next()* on it will result in an error, so you can only consume all the values of a generator once.

reference: https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

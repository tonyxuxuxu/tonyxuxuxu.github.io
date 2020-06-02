---
layout:     post
title:      "Pointers vs Reference"
subtitle:   " \"Python Leetcode整理\""
date:       2019-08-18 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - C
    - Algorithm
---

## Pointers & References deferences
```
int i = 3;

// A pointer to variable i (or stores
// address of i)
int *ptr = &i;

// A reference (or alias) for i.
int &ref = i;
```

### Intialization

Pointers:
```
int a = 10;        
 int *p = &a;    
        OR
    int *p;
  p = &a;
we can declare and initialize pointer at same step or in multiple line.
```

References:
```
int a=10;
int &p=a;  //it is correct
   but
int &p;
 p=a;    // it is incorrect as we should declare and initialize references at single step.
```

### Reassignment

A pointer can be re-assigned.

```
int a = 5;
int b = 6;
int *p;
p =  &a;
p = &b;
```

On the other hand, a reference cannot be re-assigned, and must be assigned at initialization.

```
int a = 5;
int b = 6;
int &p = a;
int &p = b;  //At this line it will show error as "multiple declaration is not allowed".

However it is valid statement,
int &q=p;
```

### Memory address

A pointer has its own memory address and size on the stack whereas a reference shares the same memory addressbut also takes up some space on the stack.

### NULL value

Pointer can be assigned NULL directly, whereas reference cannot. The constraints associated with references (no NULL, no reassignment) ensure that the underlying operations do not run into exception situation.

### Indirection

```
In Pointers,
int a = 10;
int *p;
int **q;  //it is valid.
p = &a;
q = &p;
```
Whereas in references,

```
int &p = a;
int &&q = p; //it is reference to reference, so it is an error.
```

## Using differences

For array:

In Pointers:

```
int arr[] = {10,20,30};
int *p,i ;
p = arr;
for(i = 0; i<3 ; i++)
{
cout << *p << endl;
p++;
}
```

Reference:

```
int arr[] = {10,20,30};
int &p = arr[0];
int i;
for(i = 0; i<3 ; i++)
{
cout << p << endl;
p++;  //here it will increment arr[0]++
}

```

Pointers are extremely powerful because they allows you to access addresses and manipulate their contents. But they are also extremely complex to handle. Using them correctly, they could greatly improve the efficiency and performance. On the other hand, using them incorrectly could lead to many problems, from un-readable and un-maintainable codes, to infamous bugs such as memory leaks and buffer overflow, which may expose your system to hacking. Many new languages (such as Java and C#) remove pointer from their syntax to avoid the pitfalls of pointers, by providing automatic memory management.


## 1 Pointer variable

To ease the burden of programming using numerical address and programmer-interpreted data, early programming languages (such as C) introduce the concept of variables. A variable is a named location that can store a value of a particular type. Instead of numerical addresses, names (or identifiers) are attached to certain addresses. Also, types (such as int, double, char) are associated with the contents for ease of interpretation of data.

![image](/img/in-post/MemoryAddressContent.png)

### 1.1 Pointer variable

A pointer variable (or pointer in short) is basically the same as the other variables, which can store a piece of data. Unlike normal variable which stores a value (such as an int, a double, a char), a pointer stores a memory address.

### 1.2 Declaring Pointers
```
type *ptr;   // Declare a pointer variable called ptr as a pointer of type
// or
type* ptr;
// or
type * ptr;  // I shall adopt this convention
```

### 1.3 Initializing Pointers via Address-Of Operator (&)

The address-of operator (&) operates on a variable, and returns the address of the variable.

```
int number = 88;     // An int variable with a value
int * pNumber;       // Declare a pointer variable called pNumber pointing to an int (or int pointer)
pNumber = &number;   // Assign the address of the variable number to pointer pNumber

int * pAnother = &number; // Declare another int pointer and init to address of the variable number
```

### 1.4 Indirection or Dereferencing Operator ( * )

```
int number = 88;
int * pNumber = &number;  // Declare and assign the address of variable number to pointer pNumber (0x22ccec)
cout << pNumber<< endl;   // Print the content of the pointer variable, which contain an address (0x22ccec)
cout << *pNumber << endl; // Print the value "pointed to" by the pointer, which is an int (88)
*pNumber = 99;            // Assign a value to where the pointer is pointed to, NOT to the pointer variable
cout << *pNumber << endl; // Print the new value "pointed to" by the pointer (99)
cout << number << endl;   // The value of variable number changes as well (99)
```

### 1.5 Pointer has a Type too

A pointer is associated with a type (of the value it points to), which is specified during declaration. A pointer can only hold an address of the declared type; it cannot hold an address of a different type.

### 1.6 Uninitialized pointers

### 1.7 Null Pointers

## 2. Reference variables

The main use of references is acting as function formal parameters to support pass-by-reference. In an reference variable is passed into a function, the function works on the original copy (instead of a clone copy in pass-by-value). Changes inside the function are reflected outside the function.

### 2.1 References( & )

The meaning of symbol & is different in an expression and in a declaration. When it is used in an expression, & denotes the address-of operator, which returns the address of a variable, e.g., if number is an int variable, &number returns the address of the variable number (this has been described in the above section).

However, when & is used in a declaration (including function formal parameters), it is part of the type identifier and is used to declare a reference variable (or reference or alias or alternate name). It is used to provide another name, or another reference, or alias to an existing variable.


### 2.2 How references work?

![image](/img/in-post/ReferenceIsAPointer.png)


### 2.3 References & Pointers

Pointers and references are equivalent, except:

1. A reference is a name constant for an address. You need to initialize the reference during declaration.

2. To get the value pointed to by a pointer, you need to use the dereferencing operator * (e.g., if pNumber is a int pointer, \*pNumber returns the value pointed to by pNumber. It is called dereferencing or indirection). To assign an address of a variable into a pointer, you need to use the address-of operator & (e.g., pNumber = &number).


### 2.4 Pass-by-reference into functions with reference arguments vs pointer arguments

In many situations, we may wish to modify the original copy directly (especially in passing huge object or array) to avoid the overhead of cloning. This can be done by passing a pointer of the object into the function, known as pass-by-reference.

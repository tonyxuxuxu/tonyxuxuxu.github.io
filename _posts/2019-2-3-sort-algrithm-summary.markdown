---
layout:     post
title:      "十大排序算法整理"
subtitle:   " \"主要几种排序算法整理\""
date:       2019-02-03 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Algorithm
    - Leetcode
    - Python
---

## 十大排序算法整理

概括：

![image](/img/in-post/sort_algrithm.png)

### 冒泡排序

```
def bubble_sort(collection):
    length = len(collection)
    for i in range(length):
       swapped = False
       for j in range(length - 1):
           if collection[j] > collection[j+1]:
               collection[j], collection[j+1] = collection[j+1], collection[j]
               swapped = true
    if not swapped:
        break
    return collection
```

### 选择排序

```
def selection_sort(collection):
    length = len(collection)
    for i in range(length):
        least = i
        for j in range(i+1, length):
            if collection[j] < collection[least]:
                least = j
        collection[i], collection[least] = collection[least], collection[i]
    return collection
```

### 插入排序

```
def insertion_sort(collection):
    for i in range(len(collection)):
        while i > 0 and collection[i] < collection[i-1]:
            collection[i], collection[i-1] = collection[i-1], collection[i]
            i -= 1
    return collection
```

### 希尔排序

```
def shell_sort(collection):
    length = len(collection)
    gap = int(length/2)

    while gap > 0:
        for i in range(gap, length):
            j = i
            while j >= gap and collection[j - gap] > collection[j]:
                collection[j], collection[j - gap] = collection[j - gap], collection[j]
           j -= gap
    gap /= 2
    return collection        
```

example:
```
49, 38, 65, 97, 26, 13, 27, 49, 55, 4

Gap 10/2 = 5

49, 38, 65, 97, 26, 13, 27, 49, 55, 4
1A                  1B
    2A                  2B
        3A                  3B
            4A                  4B
                5A                  5B

(49, 13) (38, 27) (65, 49) (97, 55) (26, 4)
 after sorting:
 (13, 49) (27, 38) (49, 65) (55, 97) (4, 26)

 13, 27, 49, 55, 4, 49, 38, 65, 97, 26

 Gap 5/2 = 2

 13, 27, 49, 55, 4, 49, 38, 65, 97, 26
 1A      1B      1C     1D      1E    
     2A      2B     2C      2D      2E

(13, 49, 4, 38, 97) (27, 55, 49, 65, 26)
after sorting:
(4, 13, 38, 49, 97) (26, 27, 49, 55, 65)

(4, 26, 13, 27, 38, 49, 49, 55, 97, 65)

Gap = 2/2 = 1

(4, 13, 26, 27, 38, 49, 49, 55, 65, 97)
```

### 归并排序

```
def merge_sort(collection):
    length = len(collection)
    if length > 1:
        midpoint = int(length/2)
        left_half = =merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = j = k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1

        return collection
```

### 快速排序

```
def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection[0]
        smaller = [element for element in collection[1:] if element<=pivot]
        larger = [element for element in collection[1:] if element>=pivot]
        return quick_sort(smaller) + pivot + quick_sort(larger)
```

### 堆排序

伪代码
```
# 时间复杂度：O(lgn)，维护最大堆性质的关键，假设根结点为LEFT(I)和RIGHT(i)的二叉树都是最大堆
# 通过让A[i]的值在最大堆中“逐级下降”，从而使得下标i为根结点的子树重新遵循最大堆的性质
MAX-HEAPIFY(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    # 找到i，i的左子树的根结点，i的右子树的根结点中值最大的结点
    if l <= A.heap-size and A[l] > A[i]
        largest = l
    else largest = i
    if r <= A.heap-size and A[r] > A[largest]
        largest = r
    # 若值最大的结点不是i，则把最大的值跟i指定的值交换。
    # 然后继续对原值最大的结点递归进行MAX-HEAPIFY操作
    # 若值最大的结点就是i，说明以i为根结点的子树已是最大堆，函数结束
    if largest != i
        exchange A[i] with A[largest]
        MAX-HEAPIFY(A, largest)
# 线性时间复杂度，从无序的输入数据数组中构造一个最大堆
BUILD-MAX-HEAP(A)
    A.heap-size = A.length
    for i = A.length/2 downto 1 #自底向上
        MAX-HEAPIFY(A, i)
# 时间复杂度：O(nlgn)，对一个数组进行原址排序(升序)
HEAPSORT(A)
    # 利用BUILD-MAX-HEAP将输入数组建成最大堆
    BUILD-MAX-HEAP(A) # 最大元素总是在根结点A[1]中
    for i = A.length downto 2
        exchange A[1] with A[i] # 将最大元素往后放在正确的位置i上
        A.heap-size = A.heap-size - 1 # 去掉结点n
        MAX-HEAPIFY(A, 1) # 维护，以保证去掉结点n后的堆还是最大堆
```

```
heap_size = 0
LEFT = lambda i: 2*i+1
RIGHT = lambda i: 2*i+2
def HEAPIFY(A, i):
   l, r = LEFT(i), RIGHT(i)
   largest = l if l < heap_size and A[l] > A[i] else i
   largest = r if r < heap_size and A[r] > A[largest] else largest
   if i != largest:
       A[i], A[largest] = A[largest], A[i]
       HEAPIFY(A, largest)

def BUILD_MAX_HEAP(A):
   global heap_size
   heap_size = len(A)
   for i in range(len(A)//2-1, -1, -1):
       HEAPIFY(A, i)

def HEAPSORT(A):
   global heap_size
   BUILD_MAX_HEAP(A)
   for i in range(len(A)-1, -1, -1):
       A[i], A[0] = A[0], A[i]
       heap_size -= 1
       HEAPIFY(A, 0)
```
### 计数排序

```
def count_sort(collection):
   min = 2147483647
   max = 0
   for i in collection:
       if x < min:
           min = x
       if x > max:
           max = x
   count = [0]*[max-min+1]
   for index in collection:
       count[index-min] += 1
   index = 0
   for a in range(max-min+1):
       for c in range(count[a]):
           collection[index] = a + min
           index += 1
   return collection
```


### 桶排序

```
def bucket_sort(collection):
   if not collection:
       return false
   max_len = max(collection) + 1
   book = [0 for x in range(0, max_len)]
   for i in collection:
       book[i] += 1
   return [i for i in range(0, max_len) for j in range(0, book[i])]
```

### 基数排序

```
def RadixSort(list,d):    
    for k in range(d):
        s=[[] for i in xrange(10)]
        for i in list:
            '''对于3个元素的数组[977, 87, 960]，第一轮排序首先按照个位数字相同的
               放在一个桶s[7]=[977],s[7]=[977,87],s[0]=[960]
               执行后list=[960,977,87].第二轮按照十位数，s[6]=[960],s[7]=[977]
               s[8]=[87],执行后list=[960,977,87].第三轮按照百位，s[9]=[960]
               s[9]=[960,977],s[0]=87,执行后list=[87,960,977],结束。'''
            s[i/(10**k)%10].append(i) #977/10=97(小数舍去),87/100=0
        list=[j for i in s for j in i]
    return list
```

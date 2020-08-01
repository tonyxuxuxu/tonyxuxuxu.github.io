---
layout:     post
title:      "Leetcode array类型整理 part9"
subtitle:   " \"Python Leetcode整理\""
date:       2020-07-28 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---


## 27. Remove element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

### Example 1:
```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
```

### Example 2:
```
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start
```

## 26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

### Example 1:

```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

```

### Example 2:

```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 1
        start = 0
        for i in range(1, len(nums)):
            if nums[start] != nums[i]:
                start = i
                nums[index] = nums[i]
                index += 1
        return index
```

## 80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


### Example 1:

```
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
```

### Example 2:

```
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for num in nums:
            if count < 2 or nums[count-1] != num or nums[count-2] != num:
                nums[count] = num
                count += 1
        return count
```

## 277. Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

### Example 1:

```
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

```

### Example 2:

```
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.

```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n^2)

```
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            j = 0
            while j < n:
                if i != j and knows(i, j) == True:
                    break
                j += 1
            if j == n:
                k = 0
                while k < n:
                    if knows(k, i) == False:
                        break
                    k += 1
                if k == n:
                    return i
        return -1
```

### 方法二

时间复杂度：O(n)

空间复杂度：O(1)

```
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        if not n:
            return -1
        celeb = 0
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i
        for i in range(n):
            if i == celeb:
                continue
            if not knows(i, celeb) or knows(celeb, i):
                return -1
        return celeb
```

## 41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

### Example 1:

```
Input: [1,2,0]
Output: 3
```

### Example 2:

```
Input: [3,4,-1,1]
Output: 2
```

### Example 3：

```
Input: [7,8,9,11,12]
Output: 1
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict={i:i for i in nums if i>0}
        n=len(dict)
        for i in range(1,n+1):
            if i not in dict:
                return i
        return n+1
```

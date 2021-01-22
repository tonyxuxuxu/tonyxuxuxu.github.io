---
layout:     post
title:      "Leetcode BinarySearch类型整理 part01"
subtitle:   " \"Python Leetcode整理\""
date:       2020-09-05 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---


## 278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

### Example:

```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

```

### 方法一

时间复杂度：O(logn)

空间复杂度：O(1)

```
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (left+right)//2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left
```

## 33. Search in Rotated Sorted Array

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

### Example 1:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Example 3:

```
Input: nums = [1], target = 0
Output: -1
```


### 方法一

时间复杂度：O(logn)

空间复杂度：O(1)

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

## 81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

### Example 1:

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

### Example 2:

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

### 方法一

时间复杂度：O(logn)

空间复杂度：O(1)

```
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return True
            while low < mid and nums[low] == nums[mid]:
                low += 1
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
```

## 162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

### Example 1:

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2:

```
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
```

### 方法一

时间复杂度：O(logn)

空间复杂度：O(1)

```
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    left = mid+1
            elif mid == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    right = mid-1
            elif nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                left = mid+1
            elif nums[mid] < nums[mid-1]:
                right = mid-1

```

### 方法二

时间复杂度：O(logn)

空间复杂度：O(1)

```
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (high+low)//2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low

```

## 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

### Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2:

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### 方法一

时间复杂度：O(logn)

空间复杂度：O(1)

```
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        left = low

        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        right = high

        return [left, right] if left <= right else[-1, -1]
```

## 349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

### Example 1:
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

### Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            if num in nums2:
                ans.append(num)
        return set(ans)
```

## 350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

### Example 1:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

### Example 2:
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```


### 方法一

时间复杂度：O(n)

空间复杂度：O(1)


```
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        c1 = collections.Counter(nums1)
        for num in nums2:
            if num in c1 and c1[num] > 0:
                ans.append(num)
                c1[num] -= 1
        return ans
```

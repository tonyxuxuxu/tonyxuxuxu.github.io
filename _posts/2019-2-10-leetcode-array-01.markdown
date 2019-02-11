---
layout:     post
title:      "Leetcode array类型整理 part1"
subtitle:   " \"Python Leetcode整理\""
date:       2019-02-10 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## No 1. Two Sum

### Problem：

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
### 方法一（暴力法）：

时间复杂度： O(n^2)

空间复杂度： O（1）

```
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return None
```

### 方法二（两遍哈希表）

时间复杂度： O(n)

空间复杂度： O(n)

```
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None
        hash_dict = {}
        for i in range(len(nums)):
            hash_dict[i] = nums[i]
        for i in range(len(nums)):
            temp = target - nums[i]
            for j, value in hash_dict.items():
                if temp == value and i != j:
                    return [i, j]
        return None
```
### 方法三（一遍哈希表）

时间复杂度： O(n)

空间复杂度： O(n)

```
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None

        hash_dict = {}
        for index1, value1 in enumerate(nums):
            tmp = target - value1

            for index2, value2 in hash_dict.items():
                if value2 == tmp:
                    return [index1, index2]

            hash_dict[index1] = value1

        return None
```

## No 4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

### Example 1
```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

### Example 2
```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

### 方法一（递归法）

将left A和left B放在一个集合， 并将right A 和right B放入另一个集合。 再把这两个新的集合分别命名为left_part和right_part:
```
left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
```
已知:
```
len(left_part)=len(right_part)
max(left_part) ≤ min(right_part)
```
需要实现:

```
i+j = m-i+n-j
B[j-1] ≤ A[i]
A[i-1] ≤ B[j]
```
时间复杂度： O(log(min(m,n)))

空间复杂度： O(1)

```
class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, half_len = 0, m, int((m+n+1)/2)
        while imin <= imax:
            i = int((imin + imax)/2)
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
```

### 方法二（归并排序）

时间复杂度： O((n+m)log(n+m))

空间复杂度： O(n+m)

```
class Solution:
    def findMedianSortedArrays(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        all_nums = []
        p1 = p2 = 0
        while p1 < nums1_len and p2 < nums2_len:
            if nums1[p1] < nums2[p2]:
                all_nums.append(nums1[p1])
                p1 += 1
            else:
                all_nums.append(nums2[p2])
                p2 += 1
        if p1 < nums1_len:
            while p1 < nums1_len:
                all_nums.append(nums1[p1])
                p1 += 1
        if p2 < nums2_len:
            while p2 < nums2_len:
                all_nums.append(nums2[p2])
                p2 += 1

        if (nums1_len + nums2_len) % 2 == 1:
            median = all_nums[int((nums1_len+nums2_len)/2)]
        else:
            median = (all_nums[int((nums1_len+nums2_len)/2)] + all_nums[int((nums1_len+nums2_len)/2-1)])/2
        return median
```

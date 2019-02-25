---
layout:     post
title:      "Leetcode array类型整理 part5"
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

## No 48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

**Note**

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

### Example 1:

```
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

### Example 2:

```
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

### 方法一（直接旋转法）

时间复杂度：O(n^2)

空间复杂度：O（1）

```
class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for l in range(int(n/2)):
            r = n - 1 - l
            for p in range(l, r):
                q = n - 1 - p
                cache = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = cache
```

### 方法二（倒置翻转法）

时间复杂度：O(n^2)

空间复杂度：O（1）

```
class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

## No 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Example：

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        max_val = sum = nums[0]
        for i in nums[1:]:
            if sum <= 0:
                sum = 0
            sum += i
            max_val = max(max_val, sum)
        return max_val

```

### 方法二（分治法）

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
     def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = int((l+r) / 2)

        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)

        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)

        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

     def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
```

## No 54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

### Example 1:

```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2:

```
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = []
        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for i in range(right, left, -1):
                result.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            result.append(matrix[top][left])
        elif left == right:
            for i in range(top, bottom + 1):
                result.append(matrix[i][left])
        elif top == bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
        return result
```

## No 55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

### Example 1:

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2:

```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```

### 方法一（一次循环）

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = 0
        for i in range(len(nums)-1):
            if target >= i and i + nums[i] > target:
                target = nums[i] + i
        return target >= len(nums) - 1
```


## No 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

### Example 1:

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

### Example 2:

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        result = []
        if not intervals:
            return result
        intervals.sort(key=lambda x: x.start)
        result.append(intervals[0])
        for interval in intervals[1:]:
            last_interval = result[-1]
            if last_interval.end >= interval.start:
                last_interval.end = max(interval.end, last_interval.end)
            else:
                result.append(interval)
        return result
```

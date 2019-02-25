---
layout:     post
title:      "Leetcode array类型整理 part4"
subtitle:   " \"Python Leetcode整理\""
date:       2019-02-17 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## No 34. Find First and Last Position of Element in Sorted Array

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

### 方法一（两次二分法）

时间复杂度：O(logn)

空间复杂度：O（1）

```
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        left = low

        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        right = high
        return (left, right) if left <= right else [-1, -1]
```

## No 35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

### Example 1:

```
Input: [1,3,5,6], 5
Output: 2
```

### Example 2:

```
Input: [1,3,5,6], 2
Output: 1
```

### Example 3:

```
Input: [1,3,5,6], 7
Output: 4
```

### Example 4:

```
Input: [1,3,5,6], 0
Output: 0
```

### 方法一（二分法）

```
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
```

## No 39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

**Note:**

1. All numbers (including target) will be positive integers.
2. The solution set must not contain duplicate combinations.

### Example 1:

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

### Example 2:

```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

### 方法一（DFS）

时间复杂度： O(n^2)

空间复杂度：O(n)

```
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        def dfs(remains, stack):
            if remains == 0:
                result.append(stack)
            else:
                for item in candidates:
                    if item > remains:
                        break
                    elif stack and item < stack[-1]:
                        continue
                    else:
                        dfs(remains-item, stack+[item])
```

### 方法二（回溯法）

时间复杂度： O(n^2)

空间复杂度：O(n)

```
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        def helper(candidates, target, ans):
            if target == 0:
                result.append(ans)
            for index, value in enumerate(candidates):
                if value > target:
                    break
                else:
                    helper(candidates[index:], target-value, ans+[value])

        helper(candidates, target, [])
        return result
```


## No 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.


**Note:**

1. All numbers (including target) will be positive integers.
2. The solution set must not contain duplicate combinations.

### Example 1:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

### Example 2:

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

### 方法一（DFS法）

时间复杂度： O(n^2)

空间复杂度：O(n)

```
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):

        if not target:
            result.append(path)

        for i in range(start, len(nums)):

            if i > start and nums[i] == nums[i - 1]:
                continue

            if nums[i] > target:
                break

            self.combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])
```

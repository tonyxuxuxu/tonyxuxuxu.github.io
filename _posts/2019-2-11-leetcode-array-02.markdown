---
layout:     post
title:      "Leetcode array类型整理 part2"
subtitle:   " \"Python Leetcode整理\""
date:       2019-02-11 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## No 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

![image](/img/in-post/post-leetcode-11.jpg)

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### 方法一（暴力法）

时间复杂度： O(n^2)

空间复杂度： O(1)

```
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_water = max(max_water, (j-i)*min(height[i], height[j]))
        return max_water
```

### 方法二（双指针法）

时间复杂度： O(n)

空间复杂度： O(1)

```
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        l, r = 0, len(height) - 1
        while l < r:
            max_water = max(max_water, (r-l)*min(height[r], height[l]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_water
```

## No 15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:**

The solution set must not contain duplicate triplets.

### Example

```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

### 方法一（双指针法）

时间复杂度： O(n^2)

空间复杂度： O(1)

```
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) == 0:
                    result.append(l)
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k+1] == nums[k]:
                        k -= 1
                elif sum(l) < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < len(nums)-2 and nums[i-1] == nums[i]:
                i += 1
        return result
```


## No 16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

### Example

```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

### 方法一（双指针法）

时间复杂度： O(n^2)

空间复杂度： O(1)

```
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        i = 0
        distance = pow(2, 32) - 1
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) == target:
                    return target
                if abs(target - sum(l)) < distance:
                    result = sum(l)
                    distance = abs(target - sum(l))
                elif sum(l) > target:
                    k -= 1
                else:
                    j += 1
        return result
```

## No 18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

**Note**

The solution set must not contain duplicate quadruplets.

### Example

```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

### 方法一

时间复杂度： O(n^2)

空间复杂度： O(n)

```
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        result = set()
        sumIndex = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in sumIndex:
                    sumIndex[nums[i] + nums[j]] = [(i, j)]
                else:
                    sumIndex[nums[i] + nums[j]].append((i, j))

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sumNeed = target - (nums[i] + nums[j])
                if sumNeed in sumIndex:
                    for index in sumIndex[sumNeed]:
                        if index[0] > j:
                            result.add(tuple(sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]])))
        result = [list(l) for l in result]
        return result
```

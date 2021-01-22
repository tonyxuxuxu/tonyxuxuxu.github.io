---
layout:     post
title:      "Leetcode array类型整理 part11"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-09 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

### Example 1:
```
Input: [1,3,4,2,2]
Output: 2
```

### Example 2:
```
Input: [3,1,3,4,2]
Output: 3
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return None
        num_dict = collections.Counter(nums)
        for i in num_dict:
            if num_dict[i] > 1:
                return i
        return None
```

## 135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

### Example 1:

```
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

```

### Example 2:

```
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count
```


## 330. Patching Array

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

### Example 1:

```
Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

```

### Example 2:

```
Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)


```
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        add, i, count = 1, 0, 0
        while add <= n:
            if i < len(nums) and nums[i] <= add:
                add += nums[i] # from [1, add] to [1, add + nums[i]]
                i += 1
            else:
                add += add # from [1, add] to [1, 2add]
                count += 1
        return count
```

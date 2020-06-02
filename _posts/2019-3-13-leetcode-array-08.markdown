---
layout:     post
title:      "Leetcode array类型整理 part8"
subtitle:   " \"Python Leetcode整理\""
date:       2019-03-13 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## No 120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n^2)

```
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        res = [[0 for _ in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] += res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] += res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])
```


## No 121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

### Example 1:

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

### Example 2:

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0        
        min_price, max_profit = prices[0], 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
```

## 122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

### Example 1:

```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

### Example 2:

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

### Example 3:

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([y - x for x, y in zip(prices[:-1], prices[1:]) if y > x])
```

## 152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

### Example 1:

```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

### Example 2:

```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        length = len(nums)
        max_list = [0 for _ in range(length)]
        min_list = [0 for _ in range(length)]
        max_list[0] = nums[0]
        min_list[0] = nums[0]
        res = nums[0]

        for i in range(1, length):
            max_list[i] = max(max_list[i - 1] * nums[i], max(min_list[i - 1] * nums[i], nums[i]))
            min_list[i] = min(max_list[i - 1] * nums[i], min(min_list[i - 1] * nums[i], nums[i]))
            res = max(res, max_list[i])

        return res
```

### 方法二

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result, curMax, curMin = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            curMax, curMin = max(num, num*curMax, num*curMin), min(num, num*curMax, num*curMin)
            result = max(curMax, result)
        return result
```


## No 153. Find Minimum in Rotated Sorted Array


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.


### Example 1:

```
Input: [3,4,5,1,2]
Output: 1
```

### Example 2:

```
Input: [4,5,6,7,0,1,2]
Output: 0
```

### 方法一（二分法）

时间复杂度：O(logn)

空间复杂度：O(n)


```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        mid = 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right)/2)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[mid]
```

### 方法二（递归法）

时间复杂度：O(n)

空间复杂度：O(n)


```
class Solution:
    def findMin(self, nums):
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = l + (r-l)//2
        if nums[mid] > nums[r]:
            return self.helper(nums, mid+1, r)
        else:
            return self.helper(nums, l, mid)
```

## No 162. Find Peak Element


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

### 方法一（二分法）

时间复杂度：O(logn)

空间复杂度：O(n)

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

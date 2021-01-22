---
layout:     post
title:      "Leetcode array类型整理 part11"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-05 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---
## 122. Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

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
        n = len(prices)
        if n<=1: return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[-1][0]  
```


## 123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

### Example 1:

```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

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

空间复杂度：O(1)

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_1 = buy_2 = float('inf')
        pro_1 = pro_2 = 0
        for price in prices:
            buy_1 = min(buy_1, price)
            pro_1 = max(pro_1, price - buy_1)
            buy_2 = min(buy_2, price - pro_1)
            pro_2 = max(pro_2, price - buy_2)
        return pro_2
```

### 方法二

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[None, None] for _ in range(3)] for _ in range(n)]

        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(3):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        return dp[-1][-1][0]
```

## 309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

### Example:

```
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])

        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])

        return dp[-1][0]
```

## 714. Best Time to Buy and Sell Stock with Transaction Fee

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

### Example 1:

```
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)


```
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[None, None] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]
```

## 188. Best Time to Buy and Sell Stock IV

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

### Example 1:

```
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

### Example 2:

```
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

```
### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0

        if k >= n//2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        else:  
            dp = [[[None, None] for _ in range(k+1)] for _ in range(n)]  # (n, k+1, 2)
            for i in range(n):
                dp[i][0][0] = 0
                dp[i][0][1] = -float('inf')
            for j in range(1, k+1):
                dp[0][j][0] = 0
                dp[0][j][1] = -prices[0]
            for i in range(1, n):
                for j in range(1, k+1):
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
            return dp[-1][-1][0]

```

## 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

### Example:

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
```

## 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



### Example:
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        height_left = height[left]
        height_right = height[right]
        sum_water = 0

        while(left < right):
            height_left = max(height_left, height[left])
            height_right = max(height_right, height[right])
            if height_left < height_right:
                sum_water += height_left - height[left]
                left += 1
            else:
                sum_water += height_right - height[right]
                right -= 1
        return sum_water

```


## 334. Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

### Example 1:

```
Input: [1,2,3,4,5]
Output: true
```

### Example 2:

```
Input: [5,4,3,2,1]
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)


```
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        s1 = s2 = float('inf')
        for num in nums:
            if num <= s1: s1 = num
            elif num <= s2: s2 = num
            else: return True
        return False
```

## 128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

### Example:

```
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_count = 0
        nums = set(nums)
        for num in nums:
            if num -1 in nums:
                continue
            count = 1
            while num+1 in nums:
                count += 1
                num += 1
            longest_count = max(count, longest_count)
        return longest_count

```

### 方法二

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_dict = dict()
        max_length = 0
        for num in nums:
            if num not in longest_dict:
                left = longest_dict.get(num-1, 0)
                right = longest_dict.get(num+1, 0)
                cur_length = 1 + left + right
                max_length = max(max_length, cur_length)

                longest_dict[num] = cur_length
                longest_dict[num-left] = cur_length
                longest_dict[num+right] = cur_length
        return max_length
```


## 164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.


### Example 1:

```
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

```

### Example 2:

```
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

```

### 方法一

时间复杂度：O(nlogn)

空间复杂度：O(1)

```
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_gap = 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            gap = nums[i+1] - nums[i]
            max_gap = max(max_gap, gap)
        return max_gap
```

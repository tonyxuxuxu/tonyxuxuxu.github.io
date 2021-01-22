---
layout:     post
title:      "Leetcode Dynamic Programming类型整理 part01"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-30 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---


## 70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Example 1:

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2:

```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```

## 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

### Example 1:

```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```
### Example 2:

```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

### Example 3:

```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]
```

## 375. Guess Number Higher or Lower II

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

### Example:

```
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
```


### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n)

建数组

这里我们需要创建一个二维数组。我们用dp[i][j]来代表[i,j]这个子序列最少要准备多少钱才足够用。将这个二维数组全部初始化为0。二维数组的初始化推荐以下写法：


dp = [[0] * (n+1) for _ in range(n+1)]
状态转移方程

根据上面的算法分析，我们遍历[i,j]中所有的可能，将这些字结构中最小的值存入到数组中：


dp[i][j] = min(x + max(dp[i][x-1], dp[x+1][j]) for x in range(i,j))
找初始值
这个很简单，首先dp数组在初始化的时候已经全部为0了。考虑最基本的情况[i,i+1]：这个时候我们一定猜i的，最多也就损失i刀；如果猜i+1的话，则有可能损失i+1刀，需要带更多的钱。


for i in range(1,n):
	dp[i][i+1] = i
有了以上三个步骤，这题已经做完了。剩下的就是写循环跑一下。


```
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1,n):
	        dp[i][i+1] = i
        for low in range(n-1, 0 ,-1):
	        for high in range(low+1, n+1):
		        dp[low][high] = min(x + max(dp[low][x-1], dp[x+1][high]) for x in range(low,high))
        return dp[1][n]
```

## 256. 粉刷房子

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses

### Example:

```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.

```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        dp = [[float('inf')]*3 for _ in range(len(costs))]
        for i in range(3):
            dp[0][i] = costs[0][i]
        for j in range(1, len(costs)):
            for i in range(3):
                dp[j][i] = costs[j][i] + min(dp[j-1][(i+1)%3], dp[j-1][(i+2)%3])
        return min(dp[-1])
```

## 265. Paint House II


There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

### Example:

```
Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

```

### 方法一

时间复杂度：O(nk^2)

空间复杂度：O(nk^2)

```
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        dp = [[float('inf') for _ in range(k)] for _ in range(n)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        for j in range(1, n):
            for i in range(k):
                for t in range(k):
                    if t == i: continue
                    dp[j][i] = min(dp[j][i], dp[j-1][t])
                dp[j][i] += costs[j][i]
        return min(dp[-1])

```

## 72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

### Example 1:

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

### Example 2:

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n^2)

```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        return dp[-1][-1]

```

## 12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

### Example 1:
```
Input: 3
Output: "III"
```

### Example 2:
```
Input: 4
Output: "IV"
```

### Example 3:
```
Input: 9
Output: "IX"
```

### Example 4:
```
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

### Example 5:
```
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000:'M',900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ""
        for i in d:
            while num >= i:
                num -= i
                res += d[i]
        return res
```

## 91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

### Example 1:

```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

### Example 2:
```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        num = [0 for _ in range(size+1)]
        num[0] = 1
        for i in range(1, size+1):
            t = int(s[i-1])
            if 1 <= t <= 9:
                num[i] += num[i-1]
            if i >= 2:
                t = int(s[i-2])*10 + int(s[i-1])
                if 10 <= t <= 26:
                    num[i] += num[i-2]
        return num[-1]
```

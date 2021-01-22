---
layout:     post
title:      "Leetcode Back类型整理 part01"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-18 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

### Example:

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, res, path+[nums[i]])
```


## 90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

### Example:

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            if nums[i] == nums[i-1] and i > index:
                continue
            self.dfs(nums, i+1, res, path+[nums[i]])       
```

## 77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

### Example 1:
```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

```

### Example 2:
```
Input: n = 1, k = 1
Output: [[1]]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def back(candidates, cur):
            if len(cur) == k:
                result.append(cur[:])
                return
            for i in range(len(candidates)):
                if len(cur) > 0 and candidates[i] < cur[-1]:  # 最重要是这一句实现剪枝，如果出现逆序就continue
                    continue
                cur.append(candidates[i])
                back(candidates[:i] + candidates[i + 1:], cur)
                cur.pop()

        nums = [i for i in range(1, n + 1)]
        result = []
        back(nums, [])
        return result
```

## 39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

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

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                res.append(stack)
            else:
                for item in candidates:
                    if remain < item:
                        break
                    elif stack and item < stack[-1]:
                        continue
                    else:
                        dfs(remain-item, stack+[item])
        dfs(target, [])
        return res
```

## 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

### Example 1:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
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
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(candidates, tmp):
            if sum(tmp) > target: return
            if sum(tmp) == target:
                result.append(tmp)
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(candidates[i + 1:], tmp + [candidates[i]])
            return result

        return  backtrack(candidates, [])
```

## 216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

### Example 1
```
Input: k = 3, n = 7
Output: [[1,2,4]]
```

### Example 2:
```
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def back(candidates, cur):
            if len(cur) == k and sum(cur) == n:
                result.append(cur[:])
                return
            for i in range(len(candidates)):
                if len(cur) > 0 and candidates[i] < cur[-1]:
                    continue
                cur.append(candidates[i])
                back(candidates[:i]+candidates[i+1:], cur)
                cur.pop()
        nums = [i for i in range(1, 10)]
        back(nums, [])
        return result
```

## 254. Factor Combinations

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.


### Example 1:
```
Input: 1
Output: []
```

### Example 2:
```
Input: 37
Output:[]
```
### Example 3:

```
Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
```

### Example 4:

```
Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        for i in range(2, int(n ** 0.5) + 1):
            if n%i == 0:
                comb = sorted([n//i, i])
                if comb not in res:
                    res.append(comb)
                    for item in self.getFactors(n//i):
                        comb = sorted([i]+item)
                        if comb not in res:
                            res.append(comb)
        return res

```

## 46. Permutations

Given a collection of distinct integers, return all possible permutations.

### Example:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```
### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
```

## 47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

### Example:

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def backtrace(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i>0 and nums[i-1] == nums[i]:
                    continue
                backtrace(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrace(nums, [])
        return res
```

## 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        targetindex = changedindex = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                targetindex = i-1
                break
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[targetindex]:
                changedindex = i
                break
        nums[targetindex], nums[changedindex] = nums[changedindex], nums[targetindex]
        if changedindex == targetindex == 0:
            nums.reverse()
        else:
            nums[targetindex+1:] = reversed(nums[targetindex+1:])
```

## 93. Restore IP Addresses

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

### Example 1:

```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

### Example 2:
```
Input: s = "0000"
Output: ["0.0.0.0"]
```

### Example 3:
```
Input: s = "1111"
Output: ["1.1.1.1"]
```

### Example 4:
```
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
```

### Example 5:
```
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(track, start):
            if len(track) == 4 and start == len(s):
                res.append('.'.join(track))
                return
            if len(track) == 4 and start < len(s):
                return
            for l in range(1, 4):
                if start + l - 1 >= len(s):
                    return
                if l >= 2 and s[start] == "0":
                    return
                tmp = s[start:start + l]
                if l == 3 and int(tmp) > 255:
                    return
                backtrack(track + [tmp], start + l)
        backtrack([], 0)
        return res
```

---
layout:     post
title:      "Leetcode array类型整理 part7"
subtitle:   " \"Python Leetcode整理\""
date:       2019-03-05 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## No 75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

### Example:

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one, two, three = 0, 0, len(nums) - 1
        while two <= three:
            if nums[two] == 0:
                nums[one], nums[two] = nums[two], nums[one]
                one += 1
                two += 1
            elif nums[two] == 1:
                two += 1
            else:
                nums[three], nums[two] = nums[two], nums[three]
                three -= 1
```

## No 78. Subsets

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

### 方法一（DFS法）

时间复杂度：O(n^2)

空间复杂度：O(n)

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

## No 79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

### 方法一（DFS法）

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board[0])
        col = len(board)
        for i in range(row):
            for j in range(col):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):

    80. Remove Duplicates from Sorted Array II    if len(word) == 0:
            return True

        if i < 0 or i >= len(board[0]) or j < 0 or j >= len(board) or word[0] != board[j][i]:
            return False

        temp = board[j][i]
        board[j][i] = '#'

        res = self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i, j+1) \
              or self.dfs(board, word[1:], i-1, j) or self.dfs(board, word[1:], i, j-1)
        board[j][i] = temp
        return res
```

## No 80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

### Example 1:

```
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
```

### Example 2:

```
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
```

### 方法一（DFS法）

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        count = 0
        for num in nums:
            if count < 2 or nums[count-1] != num or nums[count-2] != num:
                nums[count] = num
                count += 1
        return count
```

## No 81. Search in Rotated Sorted Array II

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

### 方法一（二分法）

时间复杂度：O(nlogn)

空间复杂度：O(n)


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


## No 88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

### Example:

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

### 方法一（归并法）

时间复杂度：O(nlogn)

空间复杂度：O(n)

```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = n + m - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        if m < 0:
            nums1[:n+1] = nums2[:n+1]

```

## No 90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

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

### 方法一（DFS法）

时间复杂度：O(n^2)

空间复杂度：O(n)

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
            self.dfs(nums, i + 1, res, path + [nums[i]])
```

## No 105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

### Example:

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return:

```
  3
 / \
9  20
  /  \
 15   7
```

### 方法一（递归法）

时间复杂度：O(n)

空间复杂度：O(n)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root_index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_index])
            root.left = self.buildTree(preorder, inorder[:root_index])
            root.right = self.buildTree(preorder, inorder[root_index+1:])
            return root
```


## No 106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

### Example:

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return:

```
  3
 / \
9  20
  /  \
 15   7
```

### 方法一（递归法）

时间复杂度：O(n)

空间复杂度：O(n)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root_index = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_index])
            root.right = self.buildTree(inorder[root_index+1:], postorder)
            root.left = self.buildTree(inorder[:root_index], postorder)
            return root
```

## No 118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

### Example:

```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        res = [[1]]
        while numRows > 1:
            res.append([1] + [a + b for a,b in zip(res[-1][:-1], res[-1][1:])] + [1])
            numRows -= 1
        return res
```

### 方法二

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
            res = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
```

## No 119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


### Example:

```
Input: 3
Output: [1,3,3,1]
```
### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [a+b for a, b in zip(row[:-1], row[1:])] + [1]
        return row
```

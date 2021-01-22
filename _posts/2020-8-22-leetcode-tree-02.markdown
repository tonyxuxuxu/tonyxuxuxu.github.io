---
layout:     post
title:      "Leetcode Tree类型整理 part02"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-22 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---


## 337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

### Example 1:

```
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

```

### Example 2:

```
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)


```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        def _rob(node):
            if not node:
                return 0,0
            left = _rob(node.left)
            right = _rob(node.right)
            robbed = node.val+left[1]+right[1]
            not_robbed = max(left)+max(right)
            return robbed, not_robbed
        return max(_rob(root))
```


## 95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

### Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        @functools.lru_cache(None)
        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
            for val in range(start, end + 1):
                for left in helper(start, val - 1):
                    for right in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return helper(1, n)

```

## 96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

### Example:

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def numTrees(self, n: int) -> int:
        store = [1, 1]
        for m in range(2, n+1):
            s = m-1
            count = 0
            for i in range(m):
                count += store[i]*store[s-i]
            store.append(count)
        return store[-1]
```

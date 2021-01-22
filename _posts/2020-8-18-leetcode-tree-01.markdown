---
layout:     post
title:      "Leetcode Tree类型整理 part01"
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

## 144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```

### 方法一(迭代法)

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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res
```


### 方法二(递归法)

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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
```

## 94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

### 方法一(迭代法)

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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res

```

## 145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```

### 方法一(迭代法)

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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res
```


## 102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
```

### 方法二

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root: return
        if len(res) == level: res.append([])
        res[level].append(root.val)
        if root.left: self.level(root.left, level + 1, res)
        if root.right: self.level(root.right, level + 1, res)
```

## 100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


### Example 1:

```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

```

### Example 2:

```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

```

### Example 3:

```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

```

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def bfs(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            return bfs(root1.left, root2.right) and bfs(root1.right, root2.left)
        return bfs(root.left, root.right)
```

## 226. Invert Binary Tree

Invert a binary tree.

### Example:

```
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

## 257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

### Example:

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        queue = [[root, []]]
        res = []
        while queue:
            node, path = queue.pop(0)
            path = path + [str(node.val)]
            if node.left:
                queue.append([node.left, path])
            if node.right:
                queue.append([node.right, path])
            if not node.left and not node.right:
                res.append('->'.join(path))
        return res
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        sub_paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return [str(root.val) + "->" + s for s in sub_paths]

```

## 112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

### Example:

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left:
            return root.val == sum
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

## 113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.


### Example:

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def dfs(root, path, sum):
            if not root:
                return
            if not root.left and not root.right and root.val == sum:
                path += [root.val]
                res.append(path)
            if  root.left:
                dfs(root.left, path+[root.val], sum-root.val)
            if root.right:
                dfs(root.right, path+[root.val], sum-root.val)
        dfs(root, [], sum)
        return res
```

## 129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.


### Example 1:

```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

```

### Example 2:

```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

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
    def sumNumbers(self, root: TreeNode) -> int:
        self.sumnum = 0
        def dfs(root, sum):
            if not root:
                return
            if not root.left and not root.right:
                sum += str(root.val)
                self.sumnum += int(sum)
            if root.left:
                dfs(root.left, sum+str(root.val))
            if root.right:
                dfs(root.right, sum+str(root.val))
        dfs(root, '')
        return self.sumnum
```

## 298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).


### Example 1:

```
Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

```


### Example 2:

```
Input:

   2
    \
     3
    /
   2    
  /
 1

Output: 2

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

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
    def longestConsecutive(self, root: TreeNode) -> int:
       if not root:
            return 0
        ans = 0

        def dfs(node, parent, parent_path):
            nonlocal ans
            if not node:
                return
            cur = 1
            if node.val == parent + 1:
                cur += parent_path

            ans = max(ans, cur)
            dfs(node.left, node.val, cur)
            dfs(node.right, node.val, cur)

        dfs(root, root.val + 1, 0)
        return ans
```

### 方法二

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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        ans = 10**9
        if root.left:
            ans = min(ans, self.minDepth(root.left))
        if root.right:
            ans = min(ans, self.minDepth(root.right))
        return ans+1
```

## 111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

### Example:

```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.min_dep = float('inf')
        def dfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                depth += 1
                self.min_dep = min(self.min_dep, depth )
            if root.left:
                dfs(root.left, depth+1)
            if root.right:
                dfs(root.right, depth+1)
        dfs(root, 0)
        return self.min_dep

```

## 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

### Example:

```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_dep = float('-inf')
        def dfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                depth += 1
                self.max_dep = max(self.max_dep, depth )
            if root.left:
                dfs(root.left, depth+1)
            if root.right:
                dfs(root.right, depth+1)
        dfs(root, 0)
        return self.max_dep
```

## 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

### Example 1:

```
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

```

### Example 2:

```
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

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
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right))+1

        return abs(height(root.left)-height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
```

## 124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

### Example 1:
```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

```

### Example 2:
```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

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
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = float('-inf')
        def dfs(r):
            if not r: return 0
            left = dfs(r.left)
            right = dfs(r.right)
            self.maxsum = max(self.maxsum, left + right + r.val)
            return max(0, max(left, right) + r.val)
        dfs(root)
        return self.maxsum
```


## 250. Count Univalue Subtrees

Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

### Example 1:

```
Input: root = [5,1,5,5,5,null,5]
Output: 4
```

### Example 2:
```
Input: root = []
Output: 0
```

### Example 3:
```
Input: root = [5,5,5,5,5,null,5]
Output: 6
```

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
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right) + (1 if self.isUnival(root) else 0)

    def isUnival(self, root):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return True
        if root.left != None and root.right == None:
            return root.val == root.left.val and self.isUnival(root.left)
        if root.left == None and root.right != None:
            return root.val == root.right.val and self.isUnival(root.right)
        if root.left != None and root.right != None:
            return root.val == root.right.val == root.left.val and self.isUnival(root.left) and self.isUnival(root.right)

```

## 366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

### Example:

```
Input: [1,2,3,4,5]
 
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]

```


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
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.res = []

        def height(node):
            if not node:
                return -1
            left = height(node.left)
            right = height(node.right)
            cur_height = max(left, right)+1
            if cur_height == len(self.res):
                self.res.append([])
            self.res[cur_height]+=[node.val]
            return cur_height

        height(root)
        return self.res

```


## 107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

3
/ \
9  20
/  \
15   7
return its bottom-up level order traversal as:

[
[15,7],
[9,20],
[3]
]

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        cur = [root]
        res = []
        while cur:
            curl = []
            nextl = []
            for node in cur:
                if node:
                    curl.append(node.val)
                    nextl.append(node.left)
                    nextl.append(node.right)
            if curl:
                res.append(curl)
            cur = nextl
        return res[::-1]

```

### 方法二

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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level(root, 0, res)
        return res[::-1]

    def level(self, root, level, res):
        if not root: return
        if len(res) == level: res.append([])
        res[level].append(root.val)
        if root.left: self.level(root.left, level + 1, res)
        if root.right: self.level(root.right, level + 1, res)
```

### 方法三

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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root:
                return res
            if depth == len(res):
                res.insert(0, [])
            res[-(depth+1)].append(root.val)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        helper(root, 0)
        return res
```

## 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

### 方法一

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root, depth):
            if not root: return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:res[depth].append(root.val)
            else: res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res
```

## 199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

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
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth > len(res):
                res.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 1)
        return res

```

## 98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

### Example 1:

```
2
/ \
1   3

Input: [2,1,3]
Output: true
```

### Example 2:

```
5
/ \
1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

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
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float('-inf'), float('inf'))
```

## 235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

### Example 1:

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

### Example 2:
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        else:
            return root
```


## 108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

### Example:

```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        length = len(nums)
        root = TreeNode(nums[length//2])
        root.left = self.sortedArrayToBST(nums[:length//2])
        root.right = self.sortedArrayToBST(nums[length//2+1:])
        return root
```

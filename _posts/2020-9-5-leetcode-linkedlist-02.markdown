---
layout:     post
title:      "Leetcode Linkedlist类型整理 part02"
subtitle:   " \"Python Leetcode整理\""
date:       2020-09-05 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

### Example 1:

```
Input: 1->2
Output: false
```

### Example 2:

```
Input: 1->2->2->1
Output: true
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num_list = []
        node = head
        while node:
            num_list.append(node.val)
            node = node.next

        for i in range(len(num_list)//2):
            if num_list[i] != num_list[len(num_list)-1-i]:
                return False
        return True
```

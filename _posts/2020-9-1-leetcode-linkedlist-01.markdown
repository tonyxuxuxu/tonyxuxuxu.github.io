---
layout:     post
title:      "Leetcode LinkedList类型整理 part01"
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

## 206. Reverse Linked List

Reverse a singly linked list.

### Example:

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            cur, prev = temp, cur
        return prev
```

## 141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

### Example 1:

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

### Example 2:

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

### Example 3:

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
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
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        quick = head.next
        while slow != quick:
            if not quick or not quick.next:
                return False
            slow = slow.next
            quick = quick.next.next
        return True
```

## 24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

### Example:

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        node = ListNode(0)
        node.next = head
        phead = node
        while phead.next and phead.next.next:
            a = phead.next
            b = phead.next.next
            phead.next = b
            a.next = b.next
            b.next = a
            phead = phead.next.next
        return node.next
```

## 328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

### Example 1:

```
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```

### Example 2:

```
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            odd = head
            even = head.next
        else:
            return None

        connect1 = odd
        connect2 = even
        while connect1.next and connect2.next:
            connect1.next = connect1.next.next
            connect2.next = connect2.next.next
            connect1 = connect1.next
            connect2 = connect2.next
        connect1.next = even
        return odd
```


## 92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

### Example:

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        a, d = dummy, dummy
        for _ in range(m - 1):
            a = a.next
        for _ in range(n):
            d = d.next
        b, c = a.next, d.next
        pre = b
        cur = pre.next
        while cur != c:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        a.next = d
        b.next = c
        return dummy.next
```

## 237. Delete Node in a Linked List

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

### 方法一

时间复杂度：O(1)

空间复杂度：O(1)


```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

## 19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

### Example:

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        quick = slow = dummy
        for _ in range(n+1):
            quick = quick.next
        while quick:
            slow = slow.next
            quick = quick.next
        slow.next = slow.next.next
        return dummy.next
```

## 83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

### Example 1:
```
Input: 1->1->2
Output: 1->2
```

### Example 2:

```
Input: 1->1->2->3->3
Output: 1->2->3
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
```

## 203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

### Example:

```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
```


## 82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

### Example 1:

```
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```

###Example 2:

```
Input: 1->1->1->2->3
Output: 2->3
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur and cur.next:
            if pre.next.val != cur.next.val:
                pre = pre.next
            else:
                while pre.next.val == cur.next.val:
                    cur = cur.next
                    if cur.next == None:
                        pre.next = None
                        break
                pre.next = cur.next
            cur = cur.next
        return dummy.next
```

## 369. Plus One Linked List

Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

### Example :

```
Input: [1,2,3]
Output: [1,2,4]
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
    def plusOne(self, head: ListNode) -> ListNode:
        res = 0
        str_res = ""
        node = head
        while node:
            str_res += str(node.val)
            node = node.next
        res = int(str_res)+1
        nextnode = None
        while res > 0:
            curnode = ListNode(res%10)
            curnode.next = nextnode
            nextnode = curnode
            res //= 10
        return curnode
```

### 方法二

时间复杂度：O(n)

空间复杂度：O(1)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def recursion(node: ListNode):
            # 终止条件: 链表尾部节点, 加1后直接返回
            if not node.next:
                node.val += 1
                return
            # 递归下一个节点
            recursion(node.next)
            # 递归完成后处理当前层节点:判断next节点是否大于0, 如果大于9的话, 减10后进位
            if node.next.val > 9:
                node.next.val -= 10
                if node.val:
                    node.val += 1
                else:
                    n = ListNode(1)
                    n.next, node.next = node.next, n


        sentry = ListNode(None)
        sentry.next = head
        recursion(sentry)
        return sentry.next

```

## 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example:

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = phead = ListNode(0)
        s = 0
        while l1 or l2 or s:
            num = (l1.val if l1 else 0)+(l2.val if l2 else 0) + s
            phead.next = ListNode(num%10)
            phead = phead.next
            s = num//10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```


## 160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


### Example 1:

```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

```

### Example 2:

```
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def length(node):
            l = 0
            while node:
                node = node.next
                l += 1
            return l

        length1, length2 = length(headA), length(headB)
        gap = abs(length1-length2)
        if length1 > length2:
            for i in range(gap):
                headA = headA.next
        else:
            for i in range(gap):
                headB = headB.next
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA
```

### 方法二

时间复杂度：O(n)

空间复杂度：O(1)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        nodeA = headA
        nodeB = headB
        while(nodeA !=nodeB):
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
```

## 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

### Example:

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        dummy = ListNode(0)
        node = dummy
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 and not l2:
            node.next = l1
        else:
            node.next = l2
        return dummy.next
```

### 方法二

时间复杂度：O(n)

空间复杂度：O(1)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
```

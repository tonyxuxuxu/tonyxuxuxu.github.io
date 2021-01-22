---
layout:     post
title:      "Leetcode string类型整理 part03"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-13 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

### Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

### Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        return s_count == t_count
```

## 49. Group Anagrams

Given an array of strings, group anagrams together.

### Example:

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for str in strs:
            temp = ''.join(sorted(list(str)))
            if temp not in str_map.keys():
                str_map[temp] = [str]
            else:
                str_map[temp].append(str)
        return list(str_map.values())
```

## Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

### Example:

```
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
```


### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        str_map = {}
        for i in range(len(strings)):
            temp = 'a'
            for j in range(len(strings[i])):
                diff = ord(strings[i][j]) - ord(strings[i][j-1])
                if diff < 0:
                    diff += 26
                temp += str(diff)
            if temp not in str_map:
                str_map[temp] = [strings[i]]
            else:
                str_map[temp].append(strings[i])

        return list(str_map.values())
```

## 87. Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.


### Example 1:
```
Input: s1 = "great", s2 = "rgeat"
Output: true
```

### Example 2:
```
Input: s1 = "abcde", s2 = "caebd"
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        len1 = len(s1)
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        for i in range(len1):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False

```

## 179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

### Example 1:
```
Input: [10,2]
Output: "210"
```

### Example 2:
```
Input: [3,30,34,5,9]
Output: "9534330"
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if str(nums[j]) + str(nums[j + 1]) > str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        ans = ""
        if nums[-1] == 0:
            return "0"
        for i in range(len(nums)-1, -1, -1):
            ans += str(nums[i])
        return ans
```

## 6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

### Example 1:

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

### Example 2:
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s

        L = ['']*numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)
```

## 161. One Edit Distance

Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t


### Example 1:
```
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
```

### Example 2:
```
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
```

### Example 3:
```
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:] == t[i:]
        return abs(len(s) - len(t)) == 1
```

## 38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

### Example 1:

```
Input: 1
Output: "1"
Explanation: This is the base case.
```

### Example 2:

```
Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".

```

具体思路
先设置上一人为'1'
开始外循环
每次外循环先置下一人为空字符串，置待处理的字符num为上一人的第一位，置记录出现的次数为1
开始内循环，遍历上一人的数，如果数是和num一致，则count增加。
若不一致，则将count和num一同添加到next_person报的数中，同时更新num和count
别忘了更新next_person的最后两个数为上一个人最后一个字符以及其出现次数！


### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1,n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1,len(prev_person)):
                if prev_person[j] == num:count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person
```

## 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



### Example:
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def find(index, s):
            if len(s) == len(digits):
                res.append(s)
                return
            for st in dict[digits[index]]:
                find(index+1, s+st)
        find(0, '')
        return res

```

## 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

### Example 1:

```
Input: s = "()"
Output: true
```

### Example 2:

```
Input: s = "()[]{}"
Output: true
```

### Example 3:
```
Input: s = "(]"
Output: false
```

### Example 4:
```
Input: s = "([)]"
Output: false
```

### Example 5:
```
Input: s = "{[]}"
Output: true
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(':')', '[':']', '{': '}'}
        for i in s:
            if i in dict:
                stack.append(i)
            elif stack:
                if dict[stack.pop()] != i:
                    return False
            else:
                return False
        return stack == []
```

## 36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

### Example 1:

```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

### Example 2:
```
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```


### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n^2)

```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [[] for _ in range(9)]
        row = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    num = int(board[j][i])
                    loc = i//3*3 + j//3
                    if num not in col[i]:
                        col[i].append(num)
                    else:
                        return False
                    if num not in row[j]:
                        row[j].append(num)
                    else:
                        return False
                    if num not in box[loc]:
                        box[loc].append(num)
                    else:
                        return False
        return True
```

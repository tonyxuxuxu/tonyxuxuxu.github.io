---
layout:     post
title:      "Leetcode string类型整理 part1"
subtitle:   " \"Python Leetcode整理\""
date:       2019-03-21 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## No 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

### Example 1:

```
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sls = len(set(s))
        slen = len(s)
        if slen < 1:
            return 0
        else:
            max_len = 1

        for i in range(slen):
            for j in range(i+max_len+1, i+sls+1):
                curr = s[i:j]
                curr_len = len(curr)
                if len(set(curr)) != curr_len:
                    break
                else:
                    if curr_len > max_len:
                        max_len = curr_len
        return max_len
```

## No 5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

### Example 1:

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```


### Example 2:

```
Input: "cbbd"
Output: "bb"
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(n)

```
class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = end = 0
        for i in range(len(s)):
            maxlensodd = self.longestPalindromeFromMiddle(i, i, s)
            maxlenseven = self.longestPalindromeFromMiddle(i, i+1, s)
            maxlen = max(maxlensodd, maxlenseven)
            if maxlen > end - start:
                start = int(i - (maxlen)/2 + 1)
                end = int(i + maxlen/2 + 1)
        return s[start: end]

    def longestPalindromeFromMiddle(self, left, right, string):
        str_lens = len(string)
        while left >= 0 and right < str_lens and string[left] == string[right]:
            left -= 1
            right += 1
        return right-left-1
```

## No 6. ZigZag Conversion

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
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
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

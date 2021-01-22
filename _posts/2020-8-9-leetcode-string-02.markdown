layout:     post
title:      "Leetcode string类型整理 part2"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-09 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### Example 1:

 ```
Input: haystack = "hello", needle = "ll"
Output: 2
 ```

### Example 2:

```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        neelen = len(needle)
        if not needle:
            return 0
        if haylen < neelen or not haystack:
            return -1
        i = 0
        while i <= haylen - neelen:
            if haystack[i:i+neelen] == needle:
                return i
            else:
                i += 1
        return -1
```

## 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Example 1:

 ```
 Input: ["flower","flow","flight"]
 Output: "fl"
 ```

### Example 2:

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        zipped = zip(*strs)
        for i in zipped:
            if len(set(i)) == 1:
                pre += i[0]
            else:
                break
        return pre

```

### 方法二


时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        n = len(strs)
        a = strs[0]
        b = strs[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res

```


## 58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

### Example:

```
Input: "Hello World"
Output: 5
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        return len(s[-1]) if s else 0
```

## 387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

### Example:

```
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_count = collections.Counter(s)
        for i in range(len(s)):
            if str_count[s[i]] == 1:
                return i
        return -1
```

## 383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.


### Example 1:

 ```
 Input: ransomNote = "a", magazine = "b"
 Output: false
 ```

### Example 2:

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```


### Example 3:

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rcount = collections.Counter(ransomNote)
        mcount = collections.Counter(magazine)
        for item, count in rcount.items():
            if item not in mcount or count > mcount[item]:
                return False
        return True
```

## 344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


### Example 1:

 ```
 Input: ["h","e","l","l","o"]
 Output: ["o","l","l","e","h"]
 ```

### Example 2:

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) -1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```


## 151. Reverse Words in a String

Given an input string, reverse the string word by word.

### Example 1:

 ```
 Input: "the sky is blue"
 Output: "blue is sky the"
 ```

### Example 2:

```
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```


### Example 3:

```
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

```

## 186. Reverse Words in a String II

Given an input string , reverse the string word by word.

### Example:

```
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)


```
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        for i in range(n):
            if s[i] == " ":
                s[left:i] = (s[left:i])[::-1]
                left = i+1
            if i == n-1:
                s[left:i+1] = (s[left:i+1])[::-1]
        s[:] = s[::-1]
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2 or not " " in s:
            return s
        n = len(s)
        right = n
        res = []
        for i in range(n-1, -1, -1):
            if right == n and s[i] == " ":
                res += s[i+1:right]
                right = i
                continue
            if s[i] == " ":
                res += s[i:right]
                right = i
            if i == 0:
                res += [" "]
                res += s[i:right]
        s[:] = res[:]

```

## 345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

### Example 1:

 ```
 Input: "hello"
 Output: "holle"
 ```

### Example 2:

```
Input: "leetcode"
Output: "leotcede"
```


### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        vlist = []
        for i in range(n):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vlist.append(i)

        nv = len(vlist)
        left, right = 0, nv-1
        while left <= right:
            s[vlist[left]], s[vlist[right]] = s[vlist[right]], s[vlist[left]]
            left += 1
            right -= 1

        return ''.join(s)     
```


## 205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.


### Example 1:

 ```
 Input: s = "egg", t = "add"
 Output: true
 ```

### Example 2:

```
Input: s = "foo", t = "bar"
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]]=t[i]
            else:
                if dic[s[i]]!=t[i]:
                    return False
        return True

```

## 293. Flip Game

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

### Example:

```
Input: s = "++++"
Output:
[
  "--++",
  "+--+",
  "++--"
]
```


### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]=='+':
                ans.append(s[:i]+'--'+s[i+2:])
        return ans
```


## 294. Flip Game II

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

### Example:

```
Input: s = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
```
### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def canWin(self, s):
        if len(s) <= 1:
            return False
        length = len(s)
        self.stateSet = {}
        return self.backtrack(s, length, True)


    def backtrack(self, s, length, player1):
        for i in range(length):
            if s[i:i + 2] == "++":
                state = (s[:i] + '--' + s[i + 2:], not player1)
                if state in self.stateSet:
                    result = self.stateSet[state]
                else:
                    result = self.backtrack(state[0], length, not player1)
                    self.stateSet[state] = result
                if result == False:
                    return True
        return False

```

## 290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

### Example 1:

```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

### Example 2:

```
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```

### Example 1:

```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

### Example 1:

```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_map = {}
        str = str.split()
        if len(str) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_map:
                if str[i] in pattern_map.values():
                    return False
                pattern_map[pattern[i]] = str[i]
            else:
                if pattern_map[pattern[i]] != str[i]:
                    return False
        return True
```

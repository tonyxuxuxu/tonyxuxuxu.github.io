---
layout:     post
title:      "Leetcode array类型整理 part10"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-01 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 299. Bulls and Cows

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

### Example 1:

```
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

```

###  Example 2:

```
Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)


```
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        d1 = collections.Counter(list(secret))
        d2 = collections.Counter(list(guess))
        for i in d1:
            if i in d2:
                cows += min(d1[i], d2[i])
        cows = cows - bulls
        return str(bulls) + 'A' + str(cows) + 'B'
```

## H-index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

```
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        length = len(citations)
        for i in range(length):
            h = length - i
            if h <= citations[i]:
                return h
        return 0
```

## 243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

### example

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

```
Input: word1 = “coding”, word2 = “practice”
Output: 3
```

```
Input: word1 = "makes", word2 = "coding"
Output: 1
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_distance = length = len(words)
        for i in range(length):
            if words[i] == word1:
                for j in range(length):
                    if words[j] == word2:
                        min_distance = min(min_distance, abs(i-j))
        return min_distance
```

### 方法二

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        m = n = min_dis = size = len(words)
        for i in range(size):
            if word1 == words[i]:
                m = i
            if word2 == words[i]:
                n = i
            if m != size and n != size:
                min_dis = min(min_dis, abs(m-n))
        return min_dis
```

## 275. H-Index II

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

```
Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
```
### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        for i in range(size):
            h = size - i
            if citations[i] >= h:
                return h
        return 0
```

### 方法二

时间复杂度：O(logn)

空间复杂度：O(1)

```
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 1:
            return 1 if citations[0] > 0 else 0
        l = 0
        r = n-1
        res = 0
        while l <= r:
            mid = l + (r - l)//2
            if citations[mid] >= n - mid:
                res = n-mid
                r = mid-1
            else:
                l = mid + 1
        return res
```

## 244. Shortest Word Distance II

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

### example

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

```
Input: word1 = “coding”, word2 = “practice”
Output: 3
```

```
Input: word1 = "makes", word2 = "coding"
Output: 1
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class WordDistance:

    def __init__(self, words: List[str]):
        self.words = words
        self.dic = {}
        for index, value in enumerate(words):
            if value in self.dic:
                self.dic[value].append(index)
            else:
                self.dic[value] = [index]


    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.dic[word1]
        list2 = self.dic[word2]
        return min(abs(a-b) for a in list1 for b in list2)



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
```

## 245. Shortest Word Distance III

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

```
Input: word1 = “coding”, word2 = “practice”
Output: 3
```

```
Input: word1 = "makes", word2 = "coding"
Output: 1
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        if not words:
            return None
        minDiff = float('inf')
        pos1 = -1
        pos2 = -1
        i = 0
        while i < len(words):
            if words[i] == word1:
                pos1 = i
                if pos2 != -1:
                    minDiff = min(minDiff, abs(pos2 - pos1))
            if words[i] == word2:
                pos2 = i
                if pos1 != -1 and pos1 != pos2:
                    minDiff = min(minDiff, abs(pos2 - pos1))
            i += 1
        return minDiff
```

## 217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

### Example 1:

```
Input: [1,2,3,1]
Output: true
```

### Example 2:

```
Input: [1,2,3,4]
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)


```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = collections.Counter(nums)
        for i in dict:
            if dict[i] >= 2:
                return True
        return False
```


### 219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


Example 1:
```
Input: nums = [1,2,3,1], k = 3
Output: true
```

Example 2:
```
Input: nums = [1,0,1,1], k = 1
Output: true
```

Example 3:
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i, value in enumerate(nums):
            if value in dict:
                if i - dict[value][-1] <= k:
                    return True
                else:
                    dict[value].append(i)
            else:
                dict[value] = [i]
        return False
```

## 220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

### Example 1:

```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

### Example 2:

```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

### Example 3:

```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 0:
            return False
        all_buckets = {}
        bucket_size = t + 1                     # 桶的大小设成t+1更加方便
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size # 放入哪个桶

            if bucket_num in all_buckets:       # 桶中已经有元素了
                return True

            all_buckets[bucket_num] = nums[i]   # 把nums[i]放入桶中

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t: # 检查前一个桶
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t: # 检查后一个桶
                return True

            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i-k]//bucket_size)

        return False
```


## 55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

### Example 1:

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

### Example 2:

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = 0
        for i in range(len(nums)-1):
            if target >= i and i + nums[i] > target:
                target = nums[i] + i
        return target >= len(nums) - 1
```


## 45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

### Example:

```
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums) -1
        position = step = 0
        while(position < length):
            if (position + nums[position] >= length):
                step += 1
                break
            else:
                max_position = maxi = 0
                for i in range(1, nums[position]):
                    if max_position < i + nums[i+position]:
                        max_position = i + nums[i+position]
                        maxi = i
                position += maxi
                step += 1
        return step
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
```

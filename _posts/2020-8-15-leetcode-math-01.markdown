---
layout:     post
title:      "Leetcode math类型整理 part01"
subtitle:   " \"Python Leetcode整理\""
date:       2020-08-15 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

### Example 1:

```
Input: 123
Output: 321
```

### Example 2:

```
Input: -123
Output: -321
```

### Example 3:

```
Input: 120
Output: 21
```

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


### 方法一

时间复杂度：O(1)

空间复杂度：O(1)

```
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            sign = -1
        else:
            sign = 1
        thenum = sign*int((str(x))[::-1])
        if thenum>=-2**31 and thenum <=2**31-1:
            return thenum
        else:
            return 0

```

## 165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.



### Example 1:

```
Input: version1 = "0.1", version2 = "1.1"
Output: -1
```

### Example 2:

```
Input: version1 = "1.0.1", version2 = "1"
Output: 1
```

### Example 3:

```
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
```

### Example 4:
```
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
```

### Example 5:
```
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.strip().split('.')
        version2 = version2.strip().split('.')
        if len(version1) < len(version2):
            version1 = version1+['0']*(len(version2)-len(version1))
        else:
            version2 = version2+['0']*(len(version1)-len(version2))
        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
            else:
                continue
        return 0
```

## 8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

### Example 1:

```
Input: "42"
Output: 42
```

### Example 2:

```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```

## Example 3:

```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```

## Example 4:

```
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
```

## Example 5:

```
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def myAtoi(self, str: str) -> int:
        numdic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        i = 0
        # 跳过前面的空白
        while i < len(str) and str[i] == ' ':
            i += 1
        # 判断异常转换情况
        if i >= len(str) or (str[i] not in numdic and str[i] not in ('+','-')):
            return 0
        # 判断正负性
        sign = 1
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
        # 提取数
        num = 0
        boundry = (1<<31)-1 if sign > 0 else 1<<31
        # 注意先判断索引，以防越界
        while i < len(str) and str[i] in numdic:
            num = num *10 + numdic[str[i]]
            i += 1
            if num > boundry:
                return sign * boundry
        return sign * num
```

## 258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.


### Example:
```
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum(list(map(int, str(num))))
        return num
```

## 67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

###  Example 1:

```
Input: a = "11", b = "1"
Output: "100"
```

### Example 2:

```
Input: a = "1010", b = "1011"
Output: "10101"
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        ans = []
        carry = 0
        i = j = 0
        while i < len(a) or j < len(b) or carry:
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[j]) if j < len(b) else 0
            carry, cur = divmod(n1+n2+carry, 2)
            ans.append(str(cur))
            i,j = i+1, j+1
        return ''.join(ans[::-1])
```

## 43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

### Example 1:
```
Input: num1 = "2", num2 = "3"
Output: "6"
```

### Example 2:
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        ans = 0
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            temp = 0
            for j in range(len(num2)):
                temp += (int(num2[j])*int(num1[i]))*10**j
            ans +=temp*10**i
        return str(ans)
```

## 69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

### Example 1:

```
Input: 4
Output: 2
```

### Example 2:

```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (r+l)//2
            if mid*mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
```

## 50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

### Example 1:

```
Input: 2.00000, 10
Output: 1024.00000
```

### Example 2:
```
Input: 2.10000, 3
Output: 9.26100
```

### Example 3:
```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
```

## 367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

### Example 1:

```
Input: num = 16
Output: true
```

### Example 2:

```
Input: num = 14
Output: false
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 0, num
        while l <= r:
            mid = (r+l)//2
            if mid*mid == num:
                return True
            if mid*mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
```

## 204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

### Example:

```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

```


### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

任何一个合数(非质数)，都可以以唯一的形式被写成有限个质数的乘积，即分解质因数。

效率提升的关键在于埃拉托斯特尼筛法，简称埃式筛，也叫厄拉多塞筛法：

要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。

```
class Solution:
    def countPrimes(self, n: int) -> int:
        List=[1]*n
        if n<3:
            return 0
        List[0],List[1]=0,0
        for i in range(2,int(n**0.5)+1):
            if  List[i]==1:
                List[i*i:n:i] = [0] * len(List[i*i:n:i])
        return sum(List)
```

## 167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.


### Example:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```


### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return None
```

## 259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

### Example:

```
Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]

```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                cur_sum = nums[i]+nums[left]+nums[right]
                if cur_sum < target:
                    res += right-left
                    left+=1
                else:
                    right-=1
        return res
```

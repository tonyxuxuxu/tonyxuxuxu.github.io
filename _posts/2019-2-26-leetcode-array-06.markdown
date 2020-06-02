---
layout:     post
title:      "Leetcode array类型整理 part6"
subtitle:   " \"Python Leetcode整理\""
date:       2019-02-21 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## No 59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

### Example:

```
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

### 方法一（环绕法）

时间复杂度：O(n)

空间复杂度：O(n^2)

```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, down, num = 0, n-1, 0, n-1, 1
        while left <= right and top <= down:
            for i in range(left, right+1):
                res[top][i] = num
                num += 1
            top += 1
            for i in range(top, down+1):
                res[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left-1, -1):
                res[down][i] = num
                num += 1
            down -= 1
            for i in range(down, top-1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res
```

### 方法二

时间复杂度：O(n)

空间复杂度：O(n^2)

```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
      A = [[0] * n for _ in range(n)]
      i, j, di, dj = 0, 0, 0, 1
      for k in range(n*n):
          A[i][j] = k + 1
          if A[(i+di)%n][(j+dj)%n]:
              di, dj = dj, -di
          i += di
          j += dj
      return A
```

## No 62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

### Example 1:

```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

### Example 2:

```
Input: m = 7, n = 3
Output: 28
```

### 方法一（DP法）

时间复杂度：O(n*m)

空间复杂度：O(n*m)

```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0]*m for _ in range(n)]
        for i in range(m):
            matrix[0][i] = 1
        for j in range(n):
            matrix[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]
        return matrix[-1][-1]
```

## No 63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

### Example 1:

```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

### 方法一（DP法）

时间复杂度：O(n*m)

空间复杂度：O(1)

```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rowLength = len(obstacleGrid[0]) # 7
        colLength = len(obstacleGrid) # 3
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, rowLength):
            if not obstacleGrid[0][i]:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            else:
                obstacleGrid[0][i] = 0

        for j in range(1, colLength):
            if not obstacleGrid[j][0]:
                obstacleGrid[j][0] = obstacleGrid[j-1][0]
            else:
                obstacleGrid[j][0] = 0

        for i in range(1, rowLength):
            for j in range(1, colLength):
                if not obstacleGrid[j][i]:
                    obstacleGrid[j][i] = obstacleGrid[j-1][i] + obstacleGrid[j][i-1]
                else:
                    obstacleGrid[j][i] = 0

        return obstacleGrid[-1][-1]

```

## No 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

### Example:

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

### 方法一（DP法）

时间复杂度：O(n*m)

空间复杂度：O(1)


```
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        rowLength = len(grid[0])
        colLength = len(grid)

        for i in range(1, rowLength):
            grid[0][i] += grid[0][i-1]

        for j in range(1, colLength):
            grid[j][0] += grid[j-1][0]

        for i in range(1, rowLength):
            for j in range(1, colLength):
                grid[j][i] += min(grid[j-1][i], grid[j][i-1])

        return grid[-1][-1]
```


## No 66. Plus One


Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

### Example 1:

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

### Example 2:

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        num = 0
        for i in digits:
            num = num*10 + i
        num += 1
        num = str(num)
        for i in num:
            result.append(int(i))
        return result
```

### 方法二（转换字符）


时间复杂度：O(n)

空间复杂度：O(n)

```
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        strDigits = ''.join(str(i) for i in digits)
        intDigits = int(strDigits) + 1
        strDigits = str(intDigits)
        for i in strDigits:
            result.append(int(i))
        return result
```

## No 73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

### Example 1:

```
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

### Example 2:

```
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

### 方法一

时间复杂度：O(n*m)

空间复杂度：O(1)

```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLength = len(matrix[0])
        colLength = len(matrix)
        rowHasZero = False
        colHasZero = False

        for i in range(rowLength):
            if matrix[0][i] == 0:
                rowHasZero = True

        for j in range(colLength):
            if matrix[j][0] == 0:
                colHasZero = True

        for i in range(1, rowLength):
            for j in range(1, colLength):
                if matrix[j][i] == 0:
                    matrix[j][0] = 0
                    matrix[0][i] = 0

        for i in range(1, rowLength):
            for j in range(1, colLength):
                if matrix[0][i] == 0 or matrix[j][0] == 0:
                    matrix[j][i] = 0

        if rowHasZero:
            for i in range(rowLength):
                matrix[0][i] = 0

        if colHasZero:
            for j in range(colLength):
                matrix[j][0] = 0
```


## No 74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

+ Integers in each row are sorted from left to right.
+ The first integer of each row is greater than the last integer of the previous row.

### Example 1:

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```

### Example 2:

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

### 方法一

时间复杂度：O(logm + logn)

空间复杂度：O(1)

```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = int((low + high) / 2)
            num = matrix[int(mid / cols)][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
```

---
layout:     post
title:      "Leetcode Matrix类型整理 part01"
subtitle:   " \"Python Leetcode整理\""
date:       2020-09-06 12:00:00
author:     "TonyXu"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Leetcode
    - Algorithm
---

## 48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

### Example 1:

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

### Example 2:

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### Example 3:

```
Input: matrix = [[1]]
Output: [[1]]
```

### Example 4:

```
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos1, pos2 = 0, len(matrix)-1
        while pos1 < pos2:
            add = 0
            while add < abs(pos1-pos2):
                temp = matrix[pos2-add][pos1]
                matrix[pos2-add][pos1] = matrix[pos2][pos2-add]
                matrix[pos2][pos2-add] = matrix[pos1+add][pos2]
                matrix[pos1+add][pos2] = matrix[pos1][pos1+add]
                matrix[pos1][pos1+add] = temp
                add += 1
            pos1 += 1
            pos2 -= 1
```


## 54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

### Example 1:

```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2:

```
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = []
        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for i in range(right, left, -1):
                result.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            result.append(matrix[top][left])
        elif left == right:
            for i in range(top, bottom + 1):
                result.append(matrix[i][left])
        elif top == bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
        return result
```

## 59. Spiral Matrix II

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

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n-1
        top, bottom = 0, n-1
        num = 1
        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = num
                num += 1
            for j in range(top, bottom):
                res[j][right] = num
                num += 1
            for i in range(right, left, -1):
                res[bottom][i] = num
                num += 1
            for j in range(bottom, top, -1):
                res[j][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            res[left][top] = num
        return res
```

## 73. Set Matrix Zeroes

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

### Example 1:

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

### Example 2:
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```


### 方法一

时间复杂度：O(nm)

空间复杂度：O(1)

```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowhaszero = colhaszero = False

        for j in range(row):
            if matrix[j][0] == 0:
                colhaszero = True

        for i in range(col):
            if matrix[0][i] == 0:
                rowhaszero = True

        for j in range(1, row):
            for i in range(1, col):
                if matrix[j][i] == 0:
                    matrix[j][0] = 0
                    matrix[0][i] = 0
        for j in range(1, row):
            if matrix[j][0] == 0:
                for i in range(1, col):
                    matrix[j][i] = 0
        for i in range(1, col):
            if matrix[0][i] == 0:
                for j in range(1, row):
                    matrix[j][i] = 0

        if colhaszero:
            for j in range(row):
                matrix[j][0] = 0

        if rowhaszero:
            for i in range(col):
                matrix[0][i] = 0

        return matrix
```

## 311. Sparse Matrix Multiplication

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

### Example:


```
Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(B[0])
        posA = self.getSparseRepresentation(A)
        posB = self.getSparseRepresentation(B)
        res = [[0 for i in range(n)] for j in range(m)]
        for valA, xA, yA in posA:
            for valB, xB, yB in posB:
                if yA == xB:
                    res[xA][yB] += valA * valB
        return res

    def getSparseRepresentation(self, A):
        posList = []
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    posList.append([A[i][j],i,j])
        return posList
```

## 74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

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

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        n = len(matrix)
        m = len(matrix[0])
        low, high = 0, n*m-1
        while low <= high:
            mid = (low+high)//2
            mid_num = matrix[mid//m][mid%m]
            if mid_num == target:
                return True
            elif mid_num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
```

## 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        m = len(matrix[0])
        n = len(matrix)
        j, i = n-1, 0
        while j >=0 and i <= m-1:
            if matrix[j][i] > target:
                j -= 1
            elif matrix[j][i] < target:
                i += 1
            else:
                return True
        return False
```

## 79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example:

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board[0])
        col = len(board)
        for i in range(row):
            for j in range(col):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):

        if len(word) == 0:
            return True

        if i < 0 or i >= len(board[0]) or j < 0 or j >= len(board) or word[0] != board[j][i]:
            return False

        temp = board[j][i]
        board[j][i] = '#'

        res = self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i, j+1) \
              or self.dfs(board, word[1:], i-1, j) or self.dfs(board, word[1:], i, j-1)
        board[j][i] = temp
        return res
```

## 361. Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

### Example:

```
Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Explanation: For the given grid,

0 E 0 0
E 0 W E
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
```

### 方法一

时间复杂度：O(n^3)

空间复杂度：O(1)

```
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        move_x, move_y = [1, 0, -1, 0], [0, 1, 0, -1]
        count = 0
        m = len(grid[0])
        n = len(grid)
        for j in range(n):
            for i in range(m):
                if grid[j][i] == "0":
                    temp = 0
                    for k in range(4):
                        y, x = j, i
                        while y >= 0 and y <= n-1 and x >= 0 and x <= m-1 and grid[y][x] != "W":
                            if grid[y][x] == "E":
                                temp += 1
                            y += move_y[k]
                            x += move_x[k]
                        count = max( temp, count )
        return count

```

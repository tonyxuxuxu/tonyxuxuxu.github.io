---
layout:     post
title:      "Leetcode DFS&BFS类型整理 part01"
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

## 200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Example 1:

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2:

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

### 方法一

时间复杂度：O(n^3)

空间复杂度：O(1)

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid[0])
        n = len(grid)
        count = 0
        for j in range(n):
            for i in range(m):
                if grid[j][i] == "1":
                    grid[j][i] = "0"
                    count += 1
                    queue = collections.deque()
                    queue.append([j,i])
                    while(len(queue)):
                        y, x = queue.popleft()
                        for new_y, new_x in ([y+1, x], [y-1, x], [y, x+1], [y, x-1]):
                            while 0<=new_x <=m-1 and 0<=new_y<=n-1 and grid[new_y][new_x] == "1":
                                grid[new_y][new_x] = "0"
                                queue.append([new_y, new_x])
        return count
```

### 方法二

时间复杂度：O(n^3)

空间复杂度：O(1)

```
class Solution:
    def dfs(self, grid, r, c):
            grid[r][c] = 0
            nr, nc = len(grid), len(grid[0])
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                    self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands
```

## 286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

### Example: 
```
Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```
### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return None
        m = len(rooms[0])
        n = len(rooms)
        que = collections.deque()
        for j in range(n):
            for i in range(m):
                if rooms[j][i] == 0:
                    que.append([j, i])

        while(que):
            y, x = que.popleft()
            for new_y, new_x in ([y+1, x], [y-1, x], [y, x+1], [y, x-1]):
                if 0 <= new_y <= n-1 and 0 <= new_x <= m-1 and rooms[new_y][new_x] == 2147483647:
                    que.append([new_y, new_x])
                    rooms[new_y][new_x] = rooms[y][x] + 1
        return rooms
```

## 130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

### Example:
```
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
```

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        m = len(board[0])
        n = len(board)
        def dfs(y ,x):
            board[y][x] = "B"
            for new_y, new_x in ([y+1, x], [y-1, x], [y, x+1], [y, x-1]):
                if 0<=new_y<=n-1 and 0<=new_x<=m-1 and board[new_y][new_x] == "O":
                    dfs(new_y, new_x)
        for i in range(m):
            if board[0][i] == "O":
                dfs(0, i)
            if board[n-1][i] == "O":
                dfs(n-1, i)

        for j in range(n):
            if board[j][0] == "O":
                dfs(j, 0)
            if board[j][m-1] == "O":
                dfs(j, m-1)

        for j in range(n):
            for i in range(m):
                if board[j][i] == "B":
                    board[j][i] = "O"
                elif board[j][i] == "O":
                    board[j][i] = "X"
```

## 339. Nested List Weight Sum

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

### Example 1:

```
Input: [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1.
```

### Example 2:

```
Input: [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
```


### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            ans = 0
            for l in nestedList:
                if l.getList():
                    ans += dfs(l.getList(), depth+1)
                elif l.getInteger():
                    ans += depth*l.getInteger()
            return ans
        return dfs(nestedList, 1)

```


## 364. Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

### Example 1:

```
Input: [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's at depth 1, one 2 at depth 2.
```

### Example 2:

```
Input: [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
```

### 方法一

时间复杂度：O(n)

空间复杂度：O(1)

```
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res, level_sum = 0, 0
        while nestedList:
            next_level = []
            for n in nestedList:
                if n.isInteger():
                    level_sum += n.getInteger()
                else:
                    next_level.extend(n.getList())
            nestedList = next_level
            res += level_sum
        return res
```

## 127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.


Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

### Example 1:

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

```


### Example 2:

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        queue = collections.deque()
        queue.append([beginWord, 1])
        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count

            for i in range(len(beginWord)):
                for j in string.ascii_lowercase:
                    check_word = word[:i] + j + word[i+1:]
                    if check_word in wordList:
                        queue.append([check_word, count+1])
                        wordList.remove(check_word)      
        return 0
```

## 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

### Example:

```
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

### 方法一

时间复杂度：O(n^2)

空间复杂度：O(1)

```
class Solution:
    def solveNQueens(self, n):
        # 生成N*N的棋盘，填充棋盘，每个格子默认是“。”表示没有放置皇后
        arr = [["." for _ in range(n)] for _ in range(n)]
        res = []
        # 检查当前的行和列是否可以放置皇后
        def check(x,y):
            # 检查竖着的一列是否有皇后
            for i in range(x):
                if arr[i][y]=="Q":
                    return False
            # 检查左上到右下的斜边是否有皇后        
            i,j = x-1,y-1
            while i>=0 and j>=0:
                if arr[i][j]=="Q":
                    return False
                i,j = i-1,j-1
            # 检查左下到右上的斜边是否有皇后    
            i,j = x-1,y+1
            while i>=0 and j<n:
                if arr[i][j]=="Q":
                    return False
                i,j = i-1,j+1
            return True
        def dfs(x):
            # x是从0开始计算的
            # 当x==n时所有行的皇后都放置完毕，此时记录结果
            if x==n:
                res.append( ["".join(arr[i]) for i in range(n)] )
                return
            # 遍历每一列    
            for y in range(n):
                # 检查[x,y]这一坐标是否可以放置皇后
                # 如果满足条件，就放置皇后，并继续检查下一行
                if check(x,y):
                    arr[x][y] = "Q"
                    dfs(x+1)
                    arr[x][y] = "."
        dfs(0)
        return res
```

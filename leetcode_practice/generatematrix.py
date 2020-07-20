class Solution:
    def generateMatrix(self, n):
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n) ]
        left, right, top, bottom = 0, n-1, 0, n-1
        while left <= right and top <= bottom:
            for i in range(left, right):
                res[top][i] = num
                num += 1
            for i in range(top, bottom):
                res[i][top] = num
                num += 1
            for i in range(right, left, -1):
                res[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                res[i][bottom] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res

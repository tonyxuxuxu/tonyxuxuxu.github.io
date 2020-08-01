class Solution:
    def generate(self, numrows):
        if not numrows:
            return []
        res = [[1]*(i+1) for i in range(numrows)]
        for i in range(numrows):
            for j in range(1, i):
                res[i][j] = res[i-1][j] + res[i-1][j-1]
        return res

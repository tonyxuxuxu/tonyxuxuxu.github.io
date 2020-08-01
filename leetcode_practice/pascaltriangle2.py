class Solution:
    def getrow(self, rowindex):
        row = [1]
        for _ in range(rowindex):
            row = [1] + [a+b for a,b in zip(row[:-1], row[1:])] + [1]
        return row

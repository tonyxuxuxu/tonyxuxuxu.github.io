class Solution:
    def rotate(self, matrix:'List[List[int]]'):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(len(matrix)):
            matrix[i] = reversed(matrix[i])


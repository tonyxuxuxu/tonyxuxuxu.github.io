class Solution:
    def setZeroes(self, matrix):
        rowlength = len(matrix[0])
        collength = len(matrix)
        rowhaszero = False
        colhaszero = False

        for i in range(rowlength):
            if matrix[0][i] == 0:
                rowhaszero = True
        
        for i in range(collength):
            if matrix[i][0] == 0:
                colhaszero = True

        for i in range(1, rowlength):
            for j in range(1, collength):
                if matrix[j][i] == 0:
                    matrix[j][0] = 0
                    matrix[0][i] = 0

        for i in range(1, rowlength):
            for j in range(1, collength):
                if matrix[j][0] == 0 or matrix[0][i] == 0:
                    matrix[j][i] = 0

        if rowhaszero:
            for i in range(rowlength):
                matrix[0][i] = 0

        if colhaszero:
            for i in range(collength):
                matrix[j][0] = 0 

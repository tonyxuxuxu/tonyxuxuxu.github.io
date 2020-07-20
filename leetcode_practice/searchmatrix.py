class Solution:
    def searchmatrix(self, matrixi, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows*cols - 1

        while low <= high:
            mid = int((high - low)/2)
            num = matrix[int(mid/col)][(mid%col)]

            if target == num:
                return True
            elif target > num:
                low = mid + 1
            else:
                high = mid - 1

        return False

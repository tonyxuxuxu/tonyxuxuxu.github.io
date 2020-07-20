class Solution:
    def plusOne(self, digit):
        result = []
        num = 0 
        for i in digit:
            num = num*10 + i
        num += 1
        num = str(num)
        for i in num:
            result.append(int(i))
        return result

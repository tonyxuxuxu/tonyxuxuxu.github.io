class Solution:
    def maxSubArray(self, nums):
        max_val = sum = 0
        for i in nums[1:]:
            if sum <= 0:
                sum = 0
            sum += i
            max_val = max(max_val, sum)
        return max_val

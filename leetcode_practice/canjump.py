class Solution:
    def canjump(self, nums):
        target = 0
        for i in range(len(nums)-1):
            if target >= i and i + nums[i] > target:
                target = nums[i] + i
        return target >= len(nums) - 1

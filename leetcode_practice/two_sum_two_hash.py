class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return None
        hashindex = {}
        for i in range(len(nums)):
            hashindex[i] = nums[i]
        for i in range(len(nums)):
            temp = target - nums[i]
            for j, value in hashindex.items():
                if value == temp and i != j:
                    return [i, j]
        return None



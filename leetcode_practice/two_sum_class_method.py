class Solution:

    @staticmethod
    def twoSum(nums, target):
        if not nums:
            return None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None



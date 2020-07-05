class Solution:
    def threeSumCloset(self, nums, target):
        nums.sort()
        result = 0
        i = 0
        distance = pow(2, 32) -1
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if abs(sum([nums[i], nums[j], nums[k]])-target) == 0:
                    return sum([nums[i], nums[j], nums[k]])
                if abs(sum([nums[i]+nums[j]+nums[k]]) - target) < distance:
                    result = sum([nums[i], nums[j], nums[k]])
                    distance = abs(sum([nums[i], nums[j], nums[k]])-target)
                if abs(sum([nums[i], nums[j], nums[k]])-target) > target:
                    k -= 1
                else:
                    j += 1
        return result

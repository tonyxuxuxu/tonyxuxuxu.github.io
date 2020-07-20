class Solution:
    def removeduplicate(self, nums):
        if not nums:
            return None
        count = 0
        for num in nums:
            if count < 2 or num != nums[count-1] or num != nums[count-2]:
                nums[count] = num
                count += 1
        return count

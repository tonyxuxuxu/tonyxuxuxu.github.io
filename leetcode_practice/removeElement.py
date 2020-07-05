class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        slow = quick = 0
        while quick < len(nums):
            if nums[quick] != val:
                nums[slow] = nums[quick]
                slow += 1
            quick += 1
        return slow

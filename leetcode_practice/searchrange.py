class Solution:
    def searchRange(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((high+low)/2)
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        left = low

        low, high = 0, len(nums) - 1
        while low <= high:
            mid  = int((high+low)/2)
            if  nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        right = high

        return [left, right] if left <= right else [-1, -1]

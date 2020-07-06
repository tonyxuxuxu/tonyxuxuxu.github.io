class Solution:
    def searchinRotatedSortedArray(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) -1 
        while low <= high:
            mid = int((high-low)/2)
            if nums[low] <= nums[mid]:
                if nums[low] <= nums[target] <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= nums[target] <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

class Solution:
    def nextPermutation(self, nums):
        targetIndex = changedIndex = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                targetIndex = i-1
                break

        for j in range(len(nums)-1, 0, -1):
            if nums[j] > nums[targetIndex]:
                changedIndex = j
                break

        nums[targetIndex], nums[changedIndex] = nums[changedIndex], nums[targetIndex]
        if changedIndex == targetIndex == 0:
            nums.reverse()
        else:
            nums[targetIndex+1:] = reversed(nums[targetIndex+1:])


class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return None
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.twoSum(nums, target))


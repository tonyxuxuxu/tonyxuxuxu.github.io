class Solution:
    def subsetswithdup(self, nums):
        res = []
        nums = sorted(nums)

        def dfs(nums, index, res, path):
            res.append(path)
            for i in range(index, len(nums)):
                if nums[i] == nums[i-1] and i > index:
                    continue
                dfs(nums, i+1, res, path+[nums[i]])

        dfs(nums, 0, res, [])
        return res

class Solution:
    def subsets(self, nums):
        if not nums:
            return None
        res = []
        def dfs(nums, index, res, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i+1, res, path+[nums[i]])

        dfs(nums, 0, res, [])
        return res

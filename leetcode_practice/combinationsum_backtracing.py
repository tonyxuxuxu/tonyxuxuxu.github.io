class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        def helper(candidates, target, ans):
            if target == 0:
                result.append(ans)
            for index, value in enumerate(candidates):
                if value > target:
                    break
                else:
                    helper(candidates[index:], target-value, ans+[value])

        helper(candidates, target, [])
        return result

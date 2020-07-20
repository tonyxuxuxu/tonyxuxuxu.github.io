class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        def combine_sum_2(nums, start, path, remains):
            if remains == 0:
                result.append(path)
            for i in range(start, len(nums)):
                if nums[i] > remains:
                    break
                elif i > start and nums[i-1] == nums[i]:
                    continue
                else:
                    combine_sum_2(nums, i+1, path+[nums[i]], remains-nums[i])
        
        combine_sum_2(candidates, 0, [], target)
        return result
            

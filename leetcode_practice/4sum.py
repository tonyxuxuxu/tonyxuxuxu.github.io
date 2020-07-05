class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        sumindex = {}
        result = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] not in sumindex:
                    sumindex[nums[i]+nums[j]] = [(i,j)]
                else:
                    sumindex[nums[i]+nums[j]].append((i,j))

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sumneed = target - nums[i] - nums[j]
                if sumneed in sumindex:
                    for index in sumindex[sumneed]:
                        if index[0] > j:
                            result.add(tuple(sorted([nums[i], nums[j], nums[index[0], nums[index[1]]]])))
        result = [list(l) for l in result]
        return result

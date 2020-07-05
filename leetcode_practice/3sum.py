class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threearr = [nums[i], nums[j], nums[k]]
                if sum(threearr) == 0:
                    result.append(threearr)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum(threearr) < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        return result



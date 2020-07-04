class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return None
        hash_dict = {}
        for index1, value1 in enumerate(nums):
            temp = target - value1
            for index2, value2 in hash_dict.items():
                if value2 == temp:
                    return [index1, index2]
            hash_dict[index1] = value1
        return None

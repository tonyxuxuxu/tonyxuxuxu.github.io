class Solution:
    def sortColors(self, nums):
        one, two, three = 0, 0, len(nums) - 1
        while two <= three:
            if nums[two] == 0:
                nums[one], nums[two] = nums[two], nums[one]
                one += 1
                two += 1
            elif nums[two] == 1:
                two += 1
            else:
                nums[two], nums[three] = nums[three], nums[two]
                three -= 1

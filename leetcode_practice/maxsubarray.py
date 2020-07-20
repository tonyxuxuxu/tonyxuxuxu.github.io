class Solution:
    def maxSubArray(self, nums):
        
        def maxSubArrayHelper(nums, l, r):
            if l > r:
                return -2147483647
            m = int((l+r)/2)
            
            leftMax = sumNum = 0
            for i in range(m-1, l-1, -1):
                sumNum = sumNum + nums[i]
                leftMax = max(sumNum, leftMax)

            rightMax = sumNum = 0
            for i in range(m+1, r+1):
                sumNum = sumNum + nums[i]
                rightMax = max(sumNum, rightMax)

            leftAns = maxSubArrayHelper(nums, l, m-1)
            rightAns = maxSubArrayHelper(nums, m+1, r)

            return max(leftMax+nums[m]+rightMax, max(leftAns, rightAns))

        return maxSubArrayHelper(nums, 0, len(nums)-1)


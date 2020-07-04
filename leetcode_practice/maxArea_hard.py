class Solution:
    def maxArea(self, height):
        max_water = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_water = max(max_water, min(height[i], height[j])*(j-i))
        return max_water

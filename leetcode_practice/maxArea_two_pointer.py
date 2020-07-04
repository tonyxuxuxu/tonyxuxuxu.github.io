class Solution:
    def maxArea(self, height):
        max_water = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_water = max(max_water, min(height[i],height[j])*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_water

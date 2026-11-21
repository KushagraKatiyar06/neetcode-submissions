class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0
        while l < r:
            if (heights[l] < heights[r]):
                currentArea = heights[l] * (r - l)
                l += 1
            else:
                currentArea = heights[r] * (r - l)
                r -= 1

            maxArea = max(currentArea, maxArea)



        return maxArea
            

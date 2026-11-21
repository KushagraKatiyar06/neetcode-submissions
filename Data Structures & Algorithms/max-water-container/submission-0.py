class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            temp_height = min(heights[left], heights[right])
            width = right - left
            area = temp_height * width
            maxArea = max(maxArea, area)

            if heights[left] < heights[right] and left < right:
                left += 1
            elif heights[right] < heights[left] and left < right:
                right -= 1
            else:
                right -= 1
            

        return maxArea
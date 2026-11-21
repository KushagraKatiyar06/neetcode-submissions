class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum =  float("-inf")
        current = 0

        for num in nums:
            current += num
            maximum = max(current, maximum)

            if current < 0:
                current = 0


        return maximum
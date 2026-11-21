class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for num in nums:
            seen.add(num)
            
        for num in nums:
            check = num
            current_streak = 1

            while check - 1 in seen:
                current_streak += 1
                check -= 1

            if current_streak > longest:
                longest = current_streak
            
        return longest
                

            
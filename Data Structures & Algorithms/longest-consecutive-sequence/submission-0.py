class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        allNums = set()
        for num in nums:
            allNums.add(num) 
        
        longest = 0

        for num in nums:
            count = 1
            current = num
            
            if (current - 1) in allNums:
                current -= 1
            else:
                while current + 1 in allNums:
                    count += 1
                    current += 1
                longest = max(longest, count)
        
        return longest

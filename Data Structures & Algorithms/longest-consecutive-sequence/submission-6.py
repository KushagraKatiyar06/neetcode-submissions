class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)

        maxSequence = 0

        for num in nums:
            currentSequence = 1

            if (num - 1) not in seen:
                while (num + currentSequence) in seen: 
                    currentSequence += 1
                if currentSequence > maxSequence:
                    maxSequence = currentSequence

        return maxSequence

            
        
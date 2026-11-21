class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        freq = {}
        currentCount = 0
        maxCount = 0

        for r in range(len(s)):
            currentCount += 1
            freq[s[r]] = freq.get(s[r], 0) + 1

            if currentCount - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
                currentCount -= 1

            maxCount = max(currentCount, (r - l + 1))
        
        return maxCount
        
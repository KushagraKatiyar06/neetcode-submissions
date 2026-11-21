class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        freq = {}
        maxCount = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            maxCount = max(maxCount, (r - l + 1))
        
        return maxCount
        
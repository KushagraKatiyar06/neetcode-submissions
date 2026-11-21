class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
            
        left = 0
        right = 0
        maxLength = 0
        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                currentLength = right - left
                maxLength = max(currentLength, maxLength)
            else:
                seen.remove(s[left])
                left += 1

        return maxLength


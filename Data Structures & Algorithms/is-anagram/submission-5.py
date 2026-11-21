class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        frequency = {}

        if len(s) != len(t):
            return False

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for char in t:
            if char not in frequency:
                return False
            else:
                frequency[char] = frequency.get(char, 0) - 1
                if frequency[char] < 0:
                    return False
        
        return True
        
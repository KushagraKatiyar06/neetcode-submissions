class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        compare = {}

        for char in s:
            if char in compare:
                compare[char] = compare[char] + 1
            else:
                compare[char] = 1

        for char in t:
            if char in compare:
                compare[char] = compare[char] - 1
                if compare[char] < 0:
                    return False
            else:
                return False

        return True
        
        
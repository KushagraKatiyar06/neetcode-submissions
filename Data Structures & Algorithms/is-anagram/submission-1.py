class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        frequency = {} # key: char, value: freq

        if len(s) != len(t):
            return False

        for char in s:
            if char in frequency:
                frequency[char] = frequency.get(char,0) + 1
            else:
                frequency[char] = 1

        for char in t:
            if char in frequency:
                frequency[char] -= 1

                if frequency[char] < 0:
                    return False
            else:
                return False

        return True
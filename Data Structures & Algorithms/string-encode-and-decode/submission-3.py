class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        if len(strs) == 0:
            return encoded

        for word in strs:
            encoded += str(len(word))
            encoded += '#'
            encoded += word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        if len(s) == 0:
            return decoded

        left = 0
        while left < len(s):
            right = left

            while s[right] != '#':
                right += 1

            currentCount = int(s[left:right])
            
            left = right + 1
            currentString = s[left : left + currentCount]
            decoded.append(currentString)

            left = left + currentCount

        return decoded
        

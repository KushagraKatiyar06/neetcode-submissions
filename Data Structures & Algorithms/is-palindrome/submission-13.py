class Solution:

    def isalum(self, s: str) -> bool:
        return (
            ord('A') <= ord(s) <= ord('Z') or
            ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9')
        )


    def isPalindrome(self, s: str) -> bool:
        l  = 0
        r = len(s) - 1

        while l < r:
            while l < r and (s[r] == " " or self.isalum(s[r]) == False):
                r -= 1

            while l < r and (s[l] == " " or self.isalum(s[l]) == False):
                l += 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
        
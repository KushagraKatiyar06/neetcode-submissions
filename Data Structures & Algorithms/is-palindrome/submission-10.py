class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0

        alpha = set('abcdefghijklmnopqrstuvwxyz0123456789')

        while right > left:
            while left < right and (s[right] == " " or s[right].lower() not in alpha):
                right -= 1
            while left < right and (s[left] == " " or s[left].lower() not in alpha):
                left += 1

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = set("0123456789abcdefghijklmnopqrstuvwxyz")

        right = len(s) - 1
        left = 0

        while left < right:
            while s[right].lower() not in alpha_num and right > left:
                right -= 1

            while s[left].lower() not in alpha_num and left < right:
                left += 1

            if s[right].lower() != s[left].lower():
                return False
            right -= 1
            left += 1

        return True
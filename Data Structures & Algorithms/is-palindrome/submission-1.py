class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        front = 0
        back = len(s) - 1

        while front < back:
            
            if  not s[back].isalnum():
                back -= 1
                continue
            
            if not s[front].isalnum():
                front += 1
                continue
    
            if s[front].lower() != s[back].lower():
                return False
            
            back -= 1
            front += 1

        return True
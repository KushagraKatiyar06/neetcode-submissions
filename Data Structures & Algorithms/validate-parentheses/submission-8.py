class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        mapping = {')' : '(', '}' : '{', ']' : '['}
        
        for char in s:
            if char in mapping:
                if seen and seen[-1] == mapping[char]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(char)

        if len(seen) != 0:
            return False

        return True
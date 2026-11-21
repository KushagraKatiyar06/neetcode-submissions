class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        mapping = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char == '(' or char == '{' or char == '[':
                seen.append(char)
            elif seen and seen[-1] == mapping[char]:
                seen.pop()

            else:
                return False
                
        return len(seen) == 0
            
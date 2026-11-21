class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)

            if char in mapping:
                if len(stack) > 0 and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
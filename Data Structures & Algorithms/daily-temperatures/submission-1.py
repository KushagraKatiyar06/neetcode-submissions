class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n-1, -1, -1):
            if len(stack) == 0:
                    result[i] = 0
            else:
                while temperatures[i] >= stack[-1][0]:
                    stack.pop()
                    if len(stack) == 0:
                        result[i] = 0
                        break
                if stack:
                    result[i] = stack[-1][1] - i
            
            stack.append(tuple((temperatures[i], i)))

        return result




        
        
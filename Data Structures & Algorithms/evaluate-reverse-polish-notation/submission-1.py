class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                a, b = stack.pop(), stack.pop()

                match token:
                    case '+':
                        stack.append(b + a)
                    case '-':
                        stack.append(b - a)
                    case '*':
                        stack.append(b * a)
                    case '/':
                        stack.append(int(b / a))

        return stack[0]
        
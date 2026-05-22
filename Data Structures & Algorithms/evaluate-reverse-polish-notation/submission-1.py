class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x)+int(y))
            elif i == "-":
                y = (stack.pop())
                x = stack.pop()
                stack.append(int(x)-int(y))
            elif i == "*":
                y = (stack.pop())
                x = stack.pop()
                stack.append(int(x)*int(y))
            elif i == "/":
                y = (stack.pop())
                x = stack.pop()
                stack.append(int(x)/int(y))
            else: 
                stack.append(i)
        return int(stack[0])
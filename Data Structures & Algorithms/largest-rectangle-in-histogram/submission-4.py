class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack  = []
        n = len(heights)
        res = 0
        for i in range(n):
            p = i
            
            while stack and stack[-1][1] >= heights[i]:
                p = stack[-1][0]
                print(p)
                x = (i - stack[-1][0]) * stack[-1][1]
                stack.pop()
                res = max(res , x)
            stack.append([p , heights[i]])
            
        print(stack)   
        s = len(stack)
        for i in range(s):
            y = stack[-1][1] * (n - stack[-1][0]) 
            stack.pop()
            res = max(res, y) 
        return res

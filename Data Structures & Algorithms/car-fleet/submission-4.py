class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        merge = list(zip(position,speed))
        merge.sort()
        n  = len(merge)
        res = []
        for i in merge :
            time = (target - i[0]) / i[1]
            stack.append(time)
        for i in range(len(stack)):
            if not stack:
                break
            x  = stack.pop()
            while stack and stack[-1] <= x:
                stack.pop()
            res.append(x)
            
        return len(res)
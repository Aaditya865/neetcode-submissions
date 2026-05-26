class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] < target:
                continue
            elif i[-1] == target:
                return True
            else :
                l = 0
                r = len(i)-2
                while l <= r :
                    n = l + ((r-l)//2)
                    if i[n] > target:
                        r = n-1
                    elif i[n] < target:
                        l = n+1
                    else :
                        return True
        return False


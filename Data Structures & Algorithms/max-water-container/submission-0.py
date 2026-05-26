class Solution:
    def maxArea(self, h: List[int]) -> int:
        res = 0
        l = 0 
        r = len(h) - 1 
        for i , n in enumerate(h):
            while l < r :
                mh = min(h[l], h[r])
                w = r-l
                res = max(res , mh * w)
                if h[l] < h[r]:
                    l += 1
                
                else:
                    r -= 1
                                        
        return res
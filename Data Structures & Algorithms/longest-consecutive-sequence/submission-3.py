class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        x = sorted(set(nums))
        m = len(x)
        res = 1
        cache = 1
        
        for i in range(m-1):
            print(x[i], x[i+1], cache)
            if (x[i]+1) == x[i+1]:
                cache += 1 
            elif (x[i]+1) != x[i+1]:
                res = max(res, cache)
                cache = 1
                
        
        res = max(res, cache)
        return res
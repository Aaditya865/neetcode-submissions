class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min (res, nums[l])
                break
            i = (l + r)//2
            if nums[i] >= nums[l]:
                res = min(res , nums[i])
                l = i + 1
            else :
                res = min(res, nums[i])
                r = i - 1
        return res

        
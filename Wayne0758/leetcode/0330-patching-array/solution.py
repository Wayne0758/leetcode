class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        x = 1
        res = 0
        i = 0
        while x<=n:
            if i < len(nums) and nums[i] <= x:
                x+=nums[i]
                i+=1
            else:
                x+=x
                res+=1
        return res

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        s = 0
        res = target+1
        for j in range(len(nums)):
            s += nums[j]
            while s>=target:
                res = min(res,j-i+1)
                s-=nums[i]
                i+=1
        if res == target+1:
            return 0
        return res

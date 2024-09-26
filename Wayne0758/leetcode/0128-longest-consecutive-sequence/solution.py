class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        nums = list(set(nums))
        nums = sorted(nums)
        res = 1
        tmp = 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                tmp+=1
                res = max(res,tmp)
            else:
                tmp = 1
        return res

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=collections.defaultdict()
        for i in range(len(nums)):
            if nums[i] in a.keys():
                a[nums[i]]+=1
            else:
                a[nums[i]]=1
        maxf=max(a.values())
        res=0
        for key in a.keys():
            if a[key] == maxf:
                res += maxf
        return res

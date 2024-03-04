class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)>=2 and nums[0] <= 0 and nums[1:]==[0] * (len(nums)-1):
            return 0
        if len(nums) == 1:
            return nums[0]
        nums=sorted(nums, key = lambda a:a**2)
        nums=nums[::-1]
        ans=1
        while nums[-1]==0:
            nums.pop()
        for i in range(len(nums)):
            ans*=nums[i]
        if ans>0:
            return int(ans)
        else:
            for i in range(len(nums)-1, -1, -1):
                if nums[i]<0:
                    ans/=nums[i]
                    return int(ans)
        return nums[0]
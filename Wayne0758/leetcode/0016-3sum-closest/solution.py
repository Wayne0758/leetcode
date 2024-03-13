class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        import math
        nums.sort()
        n=len(nums)
        min=math.inf
        ans=0
        for i in range(n-2):
            l, r = i+1, n-1
            while l<r:
                s=nums[l]+nums[i]+nums[r]
                if s==target:
                    return s
                elif s>target:
                    r -= 1
                else:
                    l += 1
                if abs(s-target)<min:
                    min=abs(s-target)
                    ans=s
        return ans

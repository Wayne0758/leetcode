class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=nums[-1]-nums[0]
        for i in range(len(nums)-1):
            high = max(nums[i]+k, nums[-1]-k)
            low = min(nums[i+1]-k, nums[0]+k)
            res = min(res, high-low)
        return res

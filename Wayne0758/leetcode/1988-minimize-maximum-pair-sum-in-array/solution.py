class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        a=[]
        for i in range(n/2):
            a.append(nums[i]+nums[n-i-1])
        return max(a)

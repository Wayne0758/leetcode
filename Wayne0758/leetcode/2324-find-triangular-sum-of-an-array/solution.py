class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for j in range(n-1):
            a=[]
            for i in range(1,len(nums)):
                a.append((nums[i]+nums[i-1])%10)
            nums=a
        return nums[0]

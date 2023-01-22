class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for i in range(len(nums)):
            if nums[i]>0:
                a+=1
            if nums[i]<0:
                b+=1
        return max(a,b)

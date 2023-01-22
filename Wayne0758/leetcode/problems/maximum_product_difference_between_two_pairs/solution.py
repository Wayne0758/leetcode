class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        nums.sort()
        a=nums[-1]*nums[-2]-nums[0]*nums[1]
        return a
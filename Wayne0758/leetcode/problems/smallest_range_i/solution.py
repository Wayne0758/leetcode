class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx=max(nums)
        mn=min(nums)
        return max(0,mx-mn-2*k)
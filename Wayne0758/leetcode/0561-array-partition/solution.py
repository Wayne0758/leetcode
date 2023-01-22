class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=0
        for i in range(len(nums)/2):
            a+=nums[2*i]
        return a

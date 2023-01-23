class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
            else:
                return nums[i]

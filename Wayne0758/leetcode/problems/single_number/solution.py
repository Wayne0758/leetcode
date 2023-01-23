class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
            else:
                a.remove(nums[i])
        return a[0]
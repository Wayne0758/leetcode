class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            a.insert(index[i],nums[i])
        return a

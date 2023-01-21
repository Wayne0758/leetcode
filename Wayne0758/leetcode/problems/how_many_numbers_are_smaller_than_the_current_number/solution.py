class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=[]
        for i in range(len(nums)):
            a=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    a+=1
            b.append(a)
        return b
        
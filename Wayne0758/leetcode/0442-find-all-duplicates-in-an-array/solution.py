class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            b=abs(nums[i])-1
            if nums[b]<0:
                a.append(b+1)
            else:
                nums[b]=-nums[b]
        return a

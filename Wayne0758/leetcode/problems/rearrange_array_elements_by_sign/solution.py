class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        c=[]
        for i in range(len(nums)):
            if nums[i]>0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        for i in range(len(nums)/2):
            c.append(a[i])
            c.append(b[i])
        return c
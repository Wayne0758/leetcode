class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                a.insert(0,nums[i])
            else:
                b.append(nums[i])
        c=[]
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        return c

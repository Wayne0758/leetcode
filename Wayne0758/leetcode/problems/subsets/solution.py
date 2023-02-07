class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        c=[]
        for i in range((2**len(nums))):
            a=bin(i)[2:]
            a=a.zfill(len(nums))
            b=[]
            for j in range(len(a)):
                if a[j]=='1':
                    b.append(nums[j])
            c.append(b)
        return c
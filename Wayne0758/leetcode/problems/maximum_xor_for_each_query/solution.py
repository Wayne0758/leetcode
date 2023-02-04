class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        a=2**maximumBit-1
        b=0
        c=[]
        for num in nums:
            b^=num
        while nums:
            c.append(b^a)
            b^=nums.pop()
        return c
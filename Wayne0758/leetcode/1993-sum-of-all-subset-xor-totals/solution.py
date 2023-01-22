class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(2**len(nums)):
            a=bin(i)[2:]
            a=a.zfill(len(nums))
            b=0
            for j in range(len(a)):
                if a[j]=="1":
                    b = b ^ nums[j]
            c+=b
        return c

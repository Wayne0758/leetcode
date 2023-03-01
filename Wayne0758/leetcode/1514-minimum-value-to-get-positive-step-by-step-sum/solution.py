class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for num in nums:
            a+=num
            if a<b:
                b=a
        return -b+1

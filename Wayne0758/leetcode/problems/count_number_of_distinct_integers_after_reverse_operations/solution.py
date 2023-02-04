class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(nums)
        for i in range(len(nums)):
            b=str(nums[i])
            b=b[::-1]
            b.lstrip('0')
            a.append(int(b))
        a=set(a)
        return len(a)
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for i in range(len(nums)):
            a+=nums[i]
            c=list(str(nums[i]))
            for j in range(len(c)):
                b+=int(c[j])
        return a-b

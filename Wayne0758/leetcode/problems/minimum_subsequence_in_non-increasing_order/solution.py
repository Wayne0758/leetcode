class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        a=[]
        for i in range(len(nums)-1,-1,-1):
            if sum(a)>sum(nums):
                return a
            else:
                a.append(nums[i])
                nums.pop()
        return a
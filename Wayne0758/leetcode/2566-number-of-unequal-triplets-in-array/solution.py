class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[i]!=nums[k]:
                        a+=1
        return a

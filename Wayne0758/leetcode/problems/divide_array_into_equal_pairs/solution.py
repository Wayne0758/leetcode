class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)/2):
            if nums[0]==nums[1]:
                nums=nums[2:]
            else:
                return False
        return True
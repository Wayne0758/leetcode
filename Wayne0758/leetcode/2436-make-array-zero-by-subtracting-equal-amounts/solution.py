class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=[]
        while 0 in nums:
            nums.remove(0)
        for i in range(len(nums)):
            if nums[i] not in b:
                b.append(nums[i])
        return len(b)

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i] not in a and nums[i] not in b:
                a.append(nums[i])
            elif nums[i] in a and nums[i] not in b:
                b.append(nums[i])
                a.remove(nums[i])
        return sum(a)

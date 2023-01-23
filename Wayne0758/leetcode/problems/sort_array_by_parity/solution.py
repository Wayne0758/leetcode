class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                a.insert(0,nums[i])
            else:
                a.append(nums[i])
        return a
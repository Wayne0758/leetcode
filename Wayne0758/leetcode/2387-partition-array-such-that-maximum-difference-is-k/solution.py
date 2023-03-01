class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        a=nums[0]+k
        res=0
        for num in nums:
            if num>a:
                a=num+k
                res+=1
        return res+1

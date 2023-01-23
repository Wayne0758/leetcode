class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        a=0
        b=0
        while nums:
            if len(nums)>1:
                if nums[0] == nums[1]:
                    nums=nums[2:]
                    a+=1
                else:
                    nums=nums[1:]
                    b+=1
            else:
                nums=[]
                b+=1
        return [a,b]

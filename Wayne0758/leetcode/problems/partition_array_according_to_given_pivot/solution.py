class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        a=[]
        b=[]
        c=[]
        for i in range(len(nums)):
            if nums[i]>pivot:
                a.append(nums[i])
            elif nums[i]<pivot:
                b.append(nums[i])
            else:
                c.append(nums[i])
        return b+c+a
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(key = lambda x:-x)
        a=[]
        for i in range(len(nums)):
            a.append([nums[i],nums.count(nums[i])])
        a.sort(key = lambda x:x[1])
        b=[]
        for i in range(len(a)):
            b.append(a[i][0])
        return b
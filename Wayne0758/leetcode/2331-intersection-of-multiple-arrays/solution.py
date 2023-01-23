class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        a=nums[0]
        b=[]
        for j in range(len(a)):
            flag=0
            for i in range(1,len(nums)):
                if a[j] not in nums[i]:
                    flag=0
                    break
                flag=1
            if flag==1:
                b.append(a[j])
        if len(nums)==1:
            b=a
        b.sort()
        return b

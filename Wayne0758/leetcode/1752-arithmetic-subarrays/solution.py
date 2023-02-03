class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        n=len(l)
        c=[]
        for i in range(n):
            begin=l[i]
            end=r[i]
            a=nums[begin:end+1]
            a.sort()
            b=a[1]-a[0]
            flag=True
            for j in range(1,len(a)):
                if a[j]-a[j-1]!=b:
                    flag=False
            c.append(flag)
        return c

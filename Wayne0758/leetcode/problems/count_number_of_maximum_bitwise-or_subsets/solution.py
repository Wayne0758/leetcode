def orq(x,y):
    return x|y
class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=reduce(orq,nums)
        d=collections.defaultdict()
        s=0
        for i in range(1,len(nums)+1):
            for c in combinations(nums,i):
                b=reduce(orq,list(c))
                if a==b:
                    s+=1
        return s
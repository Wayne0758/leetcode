class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        res=0
        now=0
        for p, g in sorted(zip(plantTime,growTime), key = lambda x:-x[1]):
            now +=p
            res=max(now+g,res)
        return res
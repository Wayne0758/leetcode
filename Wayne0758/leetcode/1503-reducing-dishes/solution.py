from functools import reduce
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True)
        pre=0
        ans=0
        for sat in satisfaction:
            pre+=sat
            if pre<0:
                break
            ans+=pre
        return ans

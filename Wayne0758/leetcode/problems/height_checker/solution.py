class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        a=sorted(heights)
        b=0
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                b+=1
        return b
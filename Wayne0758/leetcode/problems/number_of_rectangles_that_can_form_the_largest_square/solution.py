class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        a=[]
        for i in range(len(rectangles)):
            a.append(min(rectangles[i]))
        b=max(a)
        return a.count(b)
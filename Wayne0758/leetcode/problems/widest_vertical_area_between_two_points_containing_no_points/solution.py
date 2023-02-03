class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x:x[0])
        x=0
        for i in range(1,len(points)):
            y=points[i][0]-points[i-1][0]
            if y>x:
                x=y
        return x
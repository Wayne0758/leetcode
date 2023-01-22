class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        a=0
        for i in range(len(points)-1):
            a+=max(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        return a
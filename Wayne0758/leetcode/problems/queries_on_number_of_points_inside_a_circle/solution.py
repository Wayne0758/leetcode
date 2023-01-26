class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        a=[0 for i in range(len(queries))]
        for i in range(len(queries)):
            for j in range(len(points)):
                b=sqrt((points[j][0]-queries[i][0])**2+(points[j][1]-queries[i][1])**2)
                if b<=queries[i][2]:
                    a[i]+=1
        return a
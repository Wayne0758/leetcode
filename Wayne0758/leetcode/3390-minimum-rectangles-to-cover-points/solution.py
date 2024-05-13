class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        d=set()
        for point in points:
            d.add(point[0])
        a=list(d)
        a.sort()
        b=a[0]+w
        res=1
        s=0
        while a:
            if a[0]<=b:
                s=a.pop(0)
            else:
                s=a.pop(0)
                res+=1
                b=s+w
        return res

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            timePoint = timePoints[i].split(':')
            minutes = int(timePoint[0])*60+int(timePoint[1])
            timePoints[i] = minutes
        timePoints = sorted(timePoints)
        res = 1440
        for i in range(len(timePoints)):
            d = abs(timePoints[i]-timePoints[i-1])
            res = min(res,min(d,1440-d))
        return res


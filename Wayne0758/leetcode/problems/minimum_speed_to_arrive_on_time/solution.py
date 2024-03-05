class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math
        if len(dist)-1 >= hour:
            return -1
        L=math.ceil(round(float(sum(dist))/hour, 7))
        U=10**7+1
        while L!=U:
            M = int((L+U)/2)
            hourtemp=0
            for i in range(len(dist)-1):
                hourtemp += math.ceil(dist[i]/M)
            if hourtemp + dist[-1]/M <= hour:
                U=M
            else:
                L=M+1
        return L
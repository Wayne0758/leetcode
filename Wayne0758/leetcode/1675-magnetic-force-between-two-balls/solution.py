class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        l = 1
        r = position[-1] - position[0]
        def canput(force: int) -> bool:
            ball = 1
            last = position[0]
            for i in range(1, len(position)):
                if position[i]-last >= force:
                    ball+=1
                    last = position[i]
            return ball >= m
        while l<r:
            mid = (l+r+1)//2
            if canput(mid):
                l = mid
            else:
                r = mid -1
        return l

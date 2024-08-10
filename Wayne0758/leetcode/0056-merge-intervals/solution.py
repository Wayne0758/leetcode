class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            r=res[-1]
            if interval[0]<=r[1]:
                res.remove(r)
                res.append([r[0],max(r[1],interval[1])])
            else:
                res.append(interval)
        return res

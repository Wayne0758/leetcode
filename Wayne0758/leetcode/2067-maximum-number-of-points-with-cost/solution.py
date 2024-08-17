class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        pre = points[0]
        for i in range(1,m):
            left_max = [0] * n
            right_max = [0] * n
            cur = [0] * n
            left_max[0] = pre[0]
            for j in range(1,n):
                left_max[j] = max(left_max[j-1]-1, pre[j])

            right_max[-1] = pre[-1]
            for j in range(n-2,-1,-1):
                right_max[j] = max(right_max[j+1]-1, pre[j])

            for j in range(n):
                cur[j] = points[i][j] + max(left_max[j],right_max[j])
            pre = cur
        return max(pre)

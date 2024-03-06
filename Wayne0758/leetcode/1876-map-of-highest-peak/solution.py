class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        res = [[-1 for i in range(n)] for i in range(m)]
        queue = collections.deque()
        meet = set()
        d=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    queue.append((i, j))
                    meet.add((i, j))
        alt = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curx, cury = queue.popleft()
                res[curx][cury] = alt
                for dx, dy in d:
                    newx = curx + dx
                    newy = cury + dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in meet:
                        queue.append((newx, newy))
                        meet.add((newx, newy))
            alt+=1
        return res

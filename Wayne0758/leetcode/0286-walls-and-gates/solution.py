class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        queue = list()
        emptyroom = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j,0))
                    emptyroom.add((i,j))
                elif rooms[i][j] == 2147483647:
                    emptyroom.add((i,j))
        while queue:
            x,y,step = queue.pop(0)
            if (x,y) in emptyroom:
                rooms[x][y] = step
                emptyroom.remove((x,y))
                queue.append((x+1, y, step+1))
                queue.append((x-1, y, step+1))
                queue.append((x, y-1, step+1))
                queue.append((x, y+1, step+1))

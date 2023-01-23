class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a=0
        flag=0
        for i in range(len(grid)):
            flag=0
            for j in range(len(grid[i])):
                if flag==0 and grid[i][j]==1:
                    a+=2
                    flag=1
                elif flag==1 and grid[i][j]==0:
                    flag=0
        flag=0
        for j in range(len(grid[0])):
            flag=0
            for i in range(len(grid)):
                if flag==0 and grid[i][j]==1:
                    a+=2
                    flag=1
                elif flag==1 and grid[i][j]==0:
                    flag=0
        return a
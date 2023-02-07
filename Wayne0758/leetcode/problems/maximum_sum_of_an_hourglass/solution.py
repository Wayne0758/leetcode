class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a=[]
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                a.append(sum([grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]]))
        return max(a)
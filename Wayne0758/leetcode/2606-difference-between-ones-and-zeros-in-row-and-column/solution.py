class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        a=[]
        b=[0 for i in range(len(grid[0]))]
        for i in range(len(grid)):
            zerosRow=grid[i].count(0)
            onesRow=grid[i].count(1)
            a.append(onesRow-zerosRow)
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    b[j]+=1
                else:
                    b[j]-=1
        d=[]
        for i in range(len(grid)):
            c=[]
            for j in range(len(grid[0])):
                c.append(a[i]+b[j])
            d.append(c)
        return d

class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        b=[]
        s=0
        for i in range(len(grid)):
            if grid[i][0]==0:
                a=[]
                for j in range(len(grid[i])):
                    if grid[i][j]==1:
                        a.append(0)
                    else:
                        a.append(1)
                b.append(a)
            else:
                b.append(grid[i])
        n=len(grid[0])-1
        for j in range(len(grid[0])):
            zeros=0
            ones=0
            for i in range(len(grid)):
                if b[i][j]==0:
                    zeros+=1
                else:
                    ones+=1
            s+=(max(zeros,ones)*(2**(n-j)))
        return s
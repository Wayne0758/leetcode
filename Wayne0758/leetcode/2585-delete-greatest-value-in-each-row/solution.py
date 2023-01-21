class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a=0
        d=grid
        for k in range(len(grid[0])):
            e=[]
            f=0
            for i in range(len(d)):
                b=max(d[i])
                c=[]
                flag=0
                for j in d[i]:
                    if j!=b or flag!=0:
                        c.append(j)
                    if j==b and flag==0:
                        flag=1
                if b>f:
                    f=b
                e.append(c)
            a+=f
            d=e
        return a

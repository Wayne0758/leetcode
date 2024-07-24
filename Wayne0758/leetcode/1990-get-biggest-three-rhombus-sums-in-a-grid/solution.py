class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        res = []
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                count = 1
                while True:
                    s = 0
                    flag=0
                    for x in range(count):
                        y=count-1-x
                        if x!=0:
                            xlist=[x,-x]
                        else:
                            xlist=[0]
                        if y!=0:
                            ylist=[y,-y]
                        else:
                            ylist=[0]
                        for x in xlist:
                            for y in ylist:
                                if 0<=i+x<m and 0<=j+y<n:
                                    s += grid[i+x][j+y]
                                else:
                                    flag =1
                                    break
                        if flag ==1:
                            break
                    if flag ==1:
                        break
                    res.append(s)
                    count += 1
        return sorted(set(res), reverse = True)[:3]

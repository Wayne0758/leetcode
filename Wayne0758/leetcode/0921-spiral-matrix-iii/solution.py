class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        res=[[rStart,cStart]]
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        step=0
        cur=0
        while len(res)<(rows*cols):
            if cur==0 or cur==2:step+=1
            for i in range(step):
                rStart+=dirs[cur][0]
                cStart+=dirs[cur][1]
                if 0<=rStart<rows and 0<=cStart<cols:
                    res.append([rStart,cStart])
            cur=(cur+1)%4
        return res

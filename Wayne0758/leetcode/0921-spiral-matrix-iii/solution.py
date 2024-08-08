class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        d1 = [0,1,0]
        d2 = [0,-1,0]
        c = 0
        res = [[rStart, cStart]]
        cur = [rStart, cStart]
        num = rows*cols
        if num == 1:
            return res
        while True:
            c+=1
            d=[]
            if c%2==1:
                d = d1
            else:
                d = d2
            for i in range(2):
                for _ in range(c):
                    cur = [cur[0]+d[i],cur[1]+d[i+1]]
                    if 0<=cur[0]<rows and 0<=cur[1]<cols:
                        res.append(cur)
                        if len(res)==num:
                            return res

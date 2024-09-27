class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row = numRows
        n = len(s)
        part = ceil(n /(numRows-1))
        col = (numRows-1)*part
        zigzag = [[''] * col for _ in range(row)]
        d = [(1,0),(-1,1)]
        k = 0
        x=0
        y=0
        for i in range(len(s)):
            if 0<=x<row and 0<=y<col:
                zigzag[x][y] = s[i]

            else:
                x, y = x-d[k%2][0], y-d[k%2][1]
                k+=1
                x, y = x+d[k%2][0], y+d[k%2][1]
                zigzag[x][y] = s[i]
            x, y = x+d[k%2][0], y+d[k%2][1]
        res = ''
        for i in range(row):
            res += ''.join(zigzag[i])
        return res

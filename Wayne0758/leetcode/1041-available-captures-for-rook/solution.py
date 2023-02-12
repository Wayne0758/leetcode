class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m=len(board)
        n=len(board[0])
        dirs=[0,1,0,-1,0]
        a=0
        x0=0
        y0=0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='R':
                    x0=i
                    y0=j
                    break
        for k in range(4):
            dx=x0+dirs[k]
            dy=y0+dirs[k+1]
            while 0<=dx<m and 0<=dy<n:
                if board[dx][dy]=='p':
                    a+=1
                if board[dx][dy]!='.':
                    break
                dx+=dirs[k]
                dy+=dirs[k+1]
        return a

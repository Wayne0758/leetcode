class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m=len(board)
        n=len(board[0])
        cnt=0
        if m==0 or n==0:
            return 0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X' and (i==0 or board[i-1][j] =='.') and (j==0 or board[i][j-1] =='.'):
                    cnt+=1
        return cnt

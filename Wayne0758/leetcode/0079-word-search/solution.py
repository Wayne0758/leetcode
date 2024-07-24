class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x,y,remained,passed):
            if len(remained) == 0:
                return True
            d = [0,1,0,-1,0]
            for k in range(4):
                if 0<=x+d[k]<m and 0<=y+d[k+1]<n and board[x+d[k]][y+d[k+1]] == remained[0] and passed[x+d[k]][y+d[k+1]] == 0:
                    passed[x+d[k]][y+d[k+1]] = -1
                    if dfs(x+d[k],y+d[k+1],remained[1:],passed):
                        return True
                    else:
                        passed[x+d[k]][y+d[k+1]] = 0
            return False
        m = len(board)
        n = len(board[0])
        s = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    tmpwalked = [[0]*n for _ in range(m)]
                    tmpwalked[i][j] = -1
                    s-=1
                    if dfs(i,j,word[1:],tmpwalked):
                        return True
        return False

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        return m + n - (2*self.LCS(word1,word2))
    def LCS(self, text1: str, text2: str) -> int:
        m=len(text2)
        n=len(text1)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(word1)
        m = len(word2)
        length=len(s)
        dp0=[0 for _ in range(length)]
        dp1=[1 for _ in range(length)]
        dp2=[0 for _ in range(length)]
        ans=0
        for l in range(2, length+1):
            for i in range(length-l+1):
                j = i+l-1
                if s[i]==s[j]:
                    dp0[i] = dp2[i+1] + 2
                    if i<n and j>=n:
                        ans = max(ans, dp0[i])
                else:
                    dp0[i] = max(dp1[i+1],dp1[i])
            dp0, dp1, dp2 = dp2, dp0, dp1
        return ans

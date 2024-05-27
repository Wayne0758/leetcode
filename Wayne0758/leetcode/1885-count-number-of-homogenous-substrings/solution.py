class Solution:
    def countHomogenous(self, s: str) -> int:
        s+='.'
        tmp = 1
        res = 0
        kmod = 10**9+7
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                tmp = (tmp+1)
            else:
                res += ((tmp*(tmp+1)) // 2) % kmod
                tmp=1
        return res % kmod

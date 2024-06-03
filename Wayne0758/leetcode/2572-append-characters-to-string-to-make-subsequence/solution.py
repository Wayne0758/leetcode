class Solution:
    def __init__(self):
        self.s = ''
        self.t = ''
    def appendCharacters(self, s: str, t: str) -> int:
        self.s = s
        self.t = t
        res=0
        j=0
        for i in range(len(s)):
            if s[i]==t[j]:
                j+=1
                res+=1
            if j==len(t):
                break
        return len(t)-res

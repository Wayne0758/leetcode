class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        res=0
        temp=0
        n=[]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                n.append(i-temp)
                temp = i
        n.append(len(s)-temp)
        maxval=0
        for j in range(1,len(n)):
            maxval=max(maxval,n[j]+n[j-1])
        if maxval != 0:
            return maxval
        else:
            return len(s)

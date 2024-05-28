class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i=0
        j=0
        n=len(s)
        tmp=0
        cur = 0
        while j<n:
            cur += abs(ord(s[j])-ord(t[j]))
            while cur > maxCost and i<=j:
                cur -= abs(ord(s[i])-ord(t[i]))
                i+=1
            tmp=max(tmp, j-i+1)
            j+=1
        return tmp

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        a=float('inf')
        b=[]
        for i in range(len(s)):
            if s[i]==c:
                a=0
                b.append(a)
            else:
                a+=1
                b.append(a)
        a=float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i]==c:
                a=0
                b[i]=min(a,b[i])
            else:
                a+=1
                b[i]=min(a,b[i])
        return b
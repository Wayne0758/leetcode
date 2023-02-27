class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        p=range(26)
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        for i in range(len(s1)):
            r1=find(ord(s1[i])-97)
            r2=find(ord(s2[i])-97)
            if r2<r1:
                r1,r2=r2,r1
            p[r2]=r1
        res=''
        for i in range(len(baseStr)):
            res+=chr(find(ord(baseStr[i])-97)+97)
        return res
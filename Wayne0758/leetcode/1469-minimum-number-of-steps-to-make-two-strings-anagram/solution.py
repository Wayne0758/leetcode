class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l1=[0 for _ in range(26)]
        res=0
        for i in range(len(s)):
            l1[ord(s[i])-97]+=1
            l1[ord(t[i])-97]-=1
        for n in l1:
            res+=max(n,0)
        return res

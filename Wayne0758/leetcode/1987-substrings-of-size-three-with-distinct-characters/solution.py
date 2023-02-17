class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        for i in range(2,len(s)):
            n=set(s[i-2:i+1])
            if len(n)==3:
                a+=1
        return a

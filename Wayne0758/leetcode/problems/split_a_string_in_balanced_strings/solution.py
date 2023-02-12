class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        l=0
        res=0
        for i in range(len(s)):
            if s[i]=='R':
                r+=1
            elif s[i]=='L':
                l+=1
            if r==l:
                res+=1
        return res
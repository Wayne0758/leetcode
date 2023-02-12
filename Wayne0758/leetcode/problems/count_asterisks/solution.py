class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split("|")
        res=0
        for i in range(len(s)):
            if i%2==0:
                res+=s[i].count("*")
        return res
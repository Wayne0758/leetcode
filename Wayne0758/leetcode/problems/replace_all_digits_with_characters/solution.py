class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        for i in range(len(s)):
            if s[i].isdigit():
                res+=chr(ord(s[i-1])+int(s[i]))
            else:
                res+=s[i]
        return res
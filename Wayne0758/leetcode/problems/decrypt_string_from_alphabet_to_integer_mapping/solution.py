class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=''
        res=''
        for i in range(len(s)-1,-1,-1):
            if s[i]=='#':
                a+=s[i]
                continue
            if '#' in a and len(a)==1:
                a=s[i]+a
                continue
            elif '#' in a and len(a)==2:
                a=s[i]+a
                res=chr(96+int(a[:-1]))+res
                a=''
            else:
                res=chr(96+int(s[i]))+res
        return res
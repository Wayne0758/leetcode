class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        s.sort(key = lambda x:int(x[-1]))
        res=''
        for st in s:
            res+=st[:-1]
            res+=' '
        return res[:-1]
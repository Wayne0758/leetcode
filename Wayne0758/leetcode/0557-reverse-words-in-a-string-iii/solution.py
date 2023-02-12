class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        res=''
        for st in s:
            res+=st[::-1]
            res+=' '
        return res[:-1]

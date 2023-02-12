class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        l=0
        a=0
        for i in s:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            if l-r>a:
                a=l-r
        return a

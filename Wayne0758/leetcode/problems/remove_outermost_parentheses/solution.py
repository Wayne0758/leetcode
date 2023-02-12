class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=0
        r=0
        res=''
        for st in s:
            if st=='(':
                l+=1
            elif st==')':
                r+=1
            if l-r==1 and st=='(':
                continue
            elif l-r==0 and st==')':
                continue
            res+=st
        return res
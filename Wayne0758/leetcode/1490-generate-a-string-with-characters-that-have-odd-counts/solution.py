class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=''
        if n%2==0:
            for i in range(n-1):
                res+='a'
            res+='b'
            return res
        else:
            for i in range(n):
                res+='a'
            return res

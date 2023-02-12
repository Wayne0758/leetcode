class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        a,b=map(str,s.split(":"))
        res=[]
        for i in range(ord(a[0]),ord(b[0])+1):
            for j in range(int(a[1]),int(b[1])+1):
                res.append(chr(i)+str(j))
        return res
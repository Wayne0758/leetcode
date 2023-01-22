class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n=len(s)
        res=[]
        mn=0
        mx=n
        for c in s:
            if c=='I':
                res.append(mn)
                mn+=1
            else:
                res.append(mx)
                mx-=1
        res.append(mx)
        return res

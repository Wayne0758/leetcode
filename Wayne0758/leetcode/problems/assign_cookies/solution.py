class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        a=0
        while g and s:
            if s[0]>=g[0]:
                g.pop(0)
                s.pop(0)
                a+=1
            else:
                s.pop(0)
        return a
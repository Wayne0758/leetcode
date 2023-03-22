class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        ufa=range(n+1)
        b=collections.defaultdict(list)
        def find(x):
            if ufa[x]!=x:
                ufa[x]=find(ufa[x])
            return ufa[x]
        for x,y,value in roads:
            ufa_x=find(x)
            ufa_y=find(y)
            if ufa_x != ufa_y:
                ufa[ufa_x]=ufa_y
                if ufa_x in b:
                    value = min(value, b[ufa_x])
            if ufa_y in b:
                value = min(value, b[ufa_y])
            b[ufa_y] = value
        return b[find(1)]
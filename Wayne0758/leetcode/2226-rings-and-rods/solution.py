class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        d=collections.defaultdict(set)
        a=0
        for i in range(len(rings)/2):
            d[rings[2*i+1]].add(rings[2*i])
        for c in d:
            if len(d[c])==3:
                a+=1
        return a

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d=collections.defaultdict(list)
        for c in s:
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
        a=set()
        for c in d:
            a.add(d[c])
        return len(a)==1
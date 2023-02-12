class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=collections.defaultdict(list)
        for c in s:
            if c not in d:
                d[c]=1
            else:
                return c

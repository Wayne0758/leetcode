class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        res=0
        for pattern in patterns:
            if pattern in word:
                res+=1
        return res

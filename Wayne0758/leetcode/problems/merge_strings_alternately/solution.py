class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=''
        while len(word1)!=0 and len(word2)!=0:
            res+=word1[0]
            res+=word2[0]
            word1=word1[1:]
            word2=word2[1:]
        res+=word1+word2
        return res
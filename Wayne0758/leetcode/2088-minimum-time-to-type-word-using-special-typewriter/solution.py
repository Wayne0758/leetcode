class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        res=len(word)
        word='a'+word
        for i in range(1,len(word)):
            n=abs(ord(word[i])-ord(word[i-1]))
            res+=min(n,26-n)
        return res

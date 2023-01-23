class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        a=0
        for i in range(len(words)):
            if s.startswith(words[i]):
                a+=1
        return a
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        a=0
        for i in range(len(words)):
            if words[i].startswith(pref):
                a+=1
        return a
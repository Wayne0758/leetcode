class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        a=0
        for i in range(len(words)):
            flag=1
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    flag=0
            a+=flag
        return a

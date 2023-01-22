class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        s=""
        for i in range(len(words)):
            if words[i]==words[i][::-1]:
                s=words[i]
                break
        return s

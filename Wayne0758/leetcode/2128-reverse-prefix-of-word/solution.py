class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        a=''
        n=0
        for i in range(len(word)):
            if ch==word[i]:
                n=i
                break
        a=word[:n+1]
        a=a[::-1]
        a+=word[n+1:]
        return a

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        a=text.split()
        res=0
        for word in a:
            for l in brokenLetters:
                if l in word:
                    res+=1
                    break
        return len(a)-res
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        a=0
        for i in range(len(sentences)):
            b=sentences[i]
            b=list(b.split(' '))
            c=len(b)
            if c>a:
                a=c
        return a

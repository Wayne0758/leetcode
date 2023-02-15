class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        a=0
        b=0
        for i in range(len(firstWord)-1,-1,-1):
            a+=(ord(firstWord[i])-97)*(10**(len(firstWord)-1-i))
        for j in range(len(secondWord)-1,-1,-1):
            a+=(ord(secondWord[j])-97)*(10**(len(secondWord)-1-j))
        for k in range(len(targetWord)-1,-1,-1):
            b+=(ord(targetWord[k])-97)*(10**(len(targetWord)-1-k))
        return a==b

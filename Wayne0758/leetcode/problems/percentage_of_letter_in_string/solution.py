class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        a=s.count(letter)
        return int((float(a)/len(s))*100)
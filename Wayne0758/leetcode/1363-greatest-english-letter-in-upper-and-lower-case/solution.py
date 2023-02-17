class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=set(s)
        for i in range(25,-1,-1):
            if chr(65+i) in a and chr(97+i) in a:
                return chr(65+i)
        return ''

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)/2
        a=s[:n]
        b=s[n:]
        an=0
        bn=0
        vowel=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in a:
            if i in vowel:
                an+=1
        for i in b:
            if i in vowel:
                bn+=1
        return an==bn

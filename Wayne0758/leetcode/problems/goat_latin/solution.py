class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        a=sentence.split()
        vowel=['a', 'e', 'i', 'o', 'u']
        b=''
        c='maa'
        for s in a:
            if s[0].lower() in vowel:
                n=s
            else:
                n=s[1:]+s[0]
            n+=c
            b+=n+' '
            c+='a'
        return b[:-1]
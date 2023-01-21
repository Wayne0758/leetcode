class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a=[]
        table=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for s in words:
            b=""
            for c in s:
                b=b+table[ord(c)-97]
            a.append(b)
        c=[]
        d=0
        for i in range(len(a)):
            if a[i] not in c:
                c.append(a[i])
                d+=1
        return d

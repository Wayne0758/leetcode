class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        a=[]
        b=[]
        for i in range(len(words1)):
            if words1[i] not in a and words1[i] not in b:
                a.append(words1[i])
            elif words1[i] in a and words1[i] not in b:
                a.remove(words1[i])
                b.append(words1[i])
        c=[]
        d=[]
        for i in range(len(words2)):
            if words2[i] not in c and words2[i] not in d:
                c.append(words2[i])
            elif words2[i] in c and words2[i] not in d:
                c.remove(words2[i])
                d.append(words2[i])
        x=0
        for i in a:
            if i in c:
                x+=1
        return x
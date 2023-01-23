class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        for i in range(len(words)):
            a=[]
            for j in range(len(words[i])):
                if words[i][j] not in a:
                    a.append(words[i][j])
            a.sort()
            words[i]="".join(a)
        b=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j]:
                    b+=1
        return b
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=[]
        for i in range(len(words[0])):
            flag=0
            for j in range(1,len(words)):
                if words[0][i] in words[j]:
                    words[j]=words[j].replace(words[0][i],'',1)
                    flag+=1
            if flag==len(words)-1:
                a.append(words[0][i])
        return a

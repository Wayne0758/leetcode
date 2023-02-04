class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans=[]
        for word in words:
            if len(set(word))!=len(set(pattern)):
                continue
            fx=dict()
            flag=True
            for i,w in enumerate(word):
                if w in fx:
                    if fx[w] != pattern[i]:
                        flag=False
                        break
                fx[w]=pattern[i]
            if flag:
                ans.append(word)
        return ans

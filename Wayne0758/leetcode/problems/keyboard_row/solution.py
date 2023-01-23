class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=["qwertyuiop","asdfghjkl","zxcvbnm"]
        b=[]
        for i in range(len(words)):
            c=words[i].lower()
            for j in range(len(a)):
                flag=0
                if c[0] in a[j]:
                    for k in range(len(c)):
                        if c[k] not in a[j]:
                            flag=0
                            break
                        flag=1
                    if flag==1:
                        b.append(words[i])
        return b
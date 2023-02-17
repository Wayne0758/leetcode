class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        d=collections.defaultdict(list)
        for char in chars:
            if char not in d:
                d[char]=1
            else:
                d[char]+=1
        n=0
        for word in words:
            a=d.copy()
            flag=0
            for c in word:
                if c in a and a[c]>0:
                    a[c]-=1
                else:
                    flag=1
                    break
            if flag:
                continue
            n+=len(word)
        return n
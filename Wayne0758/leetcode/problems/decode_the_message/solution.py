class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        key=key.replace(' ','')
        d=collections.defaultdict(str)
        n=97
        for c in key:
            if c not in d:
                d[c]=chr(n)
                n+=1
        res=''
        for a in message:
            if a==' ':
                res+=a
                continue
            res+=d[a]
        return res
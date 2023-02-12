class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        a=[0 for _ in range(26)]
        for i in range(26):
            a[i]=s.count(chr(97+i))
        while len(ans)!=len(s):
            for i in range(26):
                if a[i]>0:
                    ans+=chr(97+i)
                    a[i]-=1
            for i in range(25,-1,-1):
                if a[i]>0:
                    ans+=chr(97+i)
                    a[i]-=1
        return ans
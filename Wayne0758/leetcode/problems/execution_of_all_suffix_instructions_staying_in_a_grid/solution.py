class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        res=[]
        for i in range(len(s)):
            a=list(startPos)
            b=len(s)-i
            for j in range(i,len(s)):
                if s[j] == 'R':
                    a[1]+=1
                elif s[j] == 'L':
                    a[1]-=1
                elif s[j] == 'U':
                    a[0]-=1
                elif s[j] == 'D':
                    a[0]+=1
                if 0<=a[0]<n and 0<=a[1]<n:
                    continue
                else:
                    b=j-i
                    break
            res.append(b)
        return res
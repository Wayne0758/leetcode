class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(len(s)):
            x=ord(s[i])-97
            if a[x]==0:
                a[x]=i+1
            else:
                b[x]=i+1
        for i in range(len(distance)):
            if a[i]!=0:
                if distance[i]+a[i]+1 != b[i]:
                    return False
        return True
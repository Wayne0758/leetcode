class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        a=[i+1 for i in range(n)]
        flag=0
        while len(a)>1:
            if flag!=(k-1):
                flag+=1
                a=a[1:]+[a[0]]
            else:
                a=a[1:]
                flag=0
        return a[0]

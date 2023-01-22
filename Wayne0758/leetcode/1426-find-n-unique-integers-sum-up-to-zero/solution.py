class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a=[]
        if n%2==0:
            for i in range(n/2):
                a.append(i+1)
                a.append(-i-1)
        if n%2==1:
            a.append(0)
            for i in range((n-1)/2):
                a.append(i+1)
                a.append(-i-1)
        return a

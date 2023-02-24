class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        a=0
        for i in n:
            if int(i)>a:
                a=int(i)
        return a

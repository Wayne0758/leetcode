class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(numRows):
            b=[]
            for j in range(i+1):
                if i==j or j==0:
                    b.append(1)
                else:
                    b.append(a[i-1][j-1]+a[i-1][j])
            a.append(b)
        return a
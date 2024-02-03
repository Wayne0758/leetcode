class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        a=[]
        ans=[]
        for i in range(2,10):
            for j in range(10-i):
                b=''
                for k in range(j,j+i):
                    b+=str(k+1)
                a.append(b)
        for st in a:
            c=int(st)
            if low<=c and c<=high:
                ans.append(int(st))
        return ans
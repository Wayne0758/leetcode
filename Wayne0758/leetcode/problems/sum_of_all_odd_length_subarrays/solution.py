class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a=int((len(arr)+1)/2)
        c=0
        for i in range(a):
            b=len(arr)-(2*i)
            for j in range(b):
                c+=sum(arr[j:j+2*i+1])
        return c
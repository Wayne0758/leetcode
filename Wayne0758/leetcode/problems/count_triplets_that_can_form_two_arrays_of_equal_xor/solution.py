from functools import reduce
def orq(x,y):
    return x^y
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s=0
        if len(arr)<2:
            return 0
        for i in range(len(arr)):
            a=arr[i]
            for j in range(i+1,len(arr)):
                a^=arr[j]
                if a==0:
                    s+=j-i
        return s
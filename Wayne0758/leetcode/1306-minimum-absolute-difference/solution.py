class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        x=arr[0]
        n=float('inf')
        a=[]
        for i in range(1,len(arr)):
            if (arr[i]-x) < n:
                n=(arr[i]-x)
            x=arr[i]
        x=arr[0]
        for i in range(1,len(arr)):
            if x+n==arr[i]:
                a.append([x,arr[i]])
            x=arr[i]
        return a

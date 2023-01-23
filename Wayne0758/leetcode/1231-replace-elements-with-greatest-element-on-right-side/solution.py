class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        a=list(arr)
        arr.append(-1)
        x=-2
        for i in range(len(arr)-1,0,-1):
            if x<arr[i]:
                x=arr[i]
                a[i-1]=x
            else:
                a[i-1]=x
        return a

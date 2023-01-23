class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        a=[]
        b=[]
        for i in range(len(arr)):
            if arr[i] not in a and arr[i] not in b:
                a.append(arr[i])
            elif arr[i] in a and arr[i] not in b:
                a.remove(arr[i])
                b.append(arr[i])
        if len(a)>=k:
            return a[k-1]
        else:
            return ""
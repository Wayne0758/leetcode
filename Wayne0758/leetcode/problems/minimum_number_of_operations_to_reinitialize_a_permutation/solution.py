class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr1=[i for i in range(n)]
        perm=list(arr1)
        arr2=list(arr1)
        res=1
        for i in range(n):
            if i%2==0:
                arr2[i]=arr1[i/2]
            else:
                arr2[i]=arr1[n/2+(i-1)/2]
        arr1=list(arr2)
        while perm!=arr1:
            for i in range(n):
                if i%2==0:
                    arr2[i]=arr1[i/2]
                else:
                    arr2[i]=arr1[n/2+(i-1)/2]
            arr1=list(arr2)
            res+=1
        return res
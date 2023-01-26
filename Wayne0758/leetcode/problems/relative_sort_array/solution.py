class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        a=[]
        c=list(arr1)
        for i in range(len(arr2)):
            b=arr1.count(arr2[i])
            for j in range(b):
                a.append(arr2[i])
                c.remove(arr2[i])
        c.sort()
        a=a+c
        return a
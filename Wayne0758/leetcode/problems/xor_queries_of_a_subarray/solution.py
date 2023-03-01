class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        xors=[0 for _ in range(len(arr)+1)]
        for i in range(1,len(arr)+1):
            xors[i]=xors[i-1]^arr[i-1]
        for a in queries:
            ans=xors[a[1]+1]^xors[a[0]]
            res.append(ans)
        return res
class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        a=[i+1 for i in range(m)]
        b=[]
        for i in range(len(queries)):
            c=[]
            for j in range(len(a)):
                if a[j]==queries[i]:
                    c=[a[j]]+c
                    b.append(j)
                else:
                    c.append(a[j])
            a=c
        return b

class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        a=items1+items2
        a.sort(key = lambda x:x[0])
        a.append([0,0])
        b=[]
        x=a[0][0]
        y=a[0][1]
        for i in range(1,len(a)):
            if a[i][0]==x:
                y+=a[i][1]
            else:
                b.append([x,y])
                x=a[i][0]
                y=a[i][1]
        return b
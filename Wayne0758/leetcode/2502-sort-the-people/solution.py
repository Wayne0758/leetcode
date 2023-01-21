class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        a=[]
        for i in range(len(names)):
            a.append([names[i],heights[i]])
        a.sort(key = lambda x: x[1])
        b=[]
        for i in range(len(a)):
            b.append(a[i][0])
        b.reverse()
        return b

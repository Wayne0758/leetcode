class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(len(image)):
            image[i].reverse()
            a.append(image[i])
        b=[]
        for i in range(len(a)):
            c=[]
            for j in range(len(a[i])):
                if a[i][j]==0:
                    c.append(1)
                else:
                    c.append(0)
            b.append(c)
        return b